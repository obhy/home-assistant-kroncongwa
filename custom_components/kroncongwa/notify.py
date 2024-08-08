import logging
import requests

from homeassistant.components.notify import (
    ATTR_DATA,
    ATTR_TARGET,
    PLATFORM_SCHEMA,
    BaseNotificationService,
)
from homeassistant.const import CONF_API_KEY, CONF_NAME
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

_LOGGER = logging.getLogger(__name__)

KRONCONGWA_API_ENDPOINT = "http://notify.obhy.net/send-message"

CONF_SENDER = 'sender'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_KEY): cv.string,
    vol.Required(CONF_SENDER): cv.string,
})

def send_whatsapp_text_message(to, message, api_key, sender):
    params = {
        'api_key': api_key,
        'sender': sender,
        'number': to,
        'message': message
    }

    resp = requests.get(KRONCONGWA_API_ENDPOINT, params=params)

    if resp.status_code == 200:
        return True

    _LOGGER.warning(
        "KroncongWA HTTP API Response: %d - %s", resp.status_code, resp.text
    )

    return False

class KroncongWANotificationService(BaseNotificationService):
    def __init__(self, api_key, sender):
        self.api_key = api_key
        self.sender = sender

    def send_message(self, message="", **kwargs):
        targets = kwargs.get(ATTR_TARGET)
        data = kwargs.get(ATTR_DATA) or {}

        if not targets:
            _LOGGER.info("At least 1 target is required")
            return

        for target in targets:
            send_whatsapp_text_message(target, message, self.api_key, self.sender)

def get_service(hass, config, discovery_info=None):
    return KroncongWANotificationService(config[CONF_API_KEY], config[CONF_SENDER])
