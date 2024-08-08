Home Assistant KroncongWA Integration

Send Home Assistant notifications to WhatsApp using [KroncongWA](http://notify.obhy.net).

```markdown

## Installation via HACS

1. **Add Custom Repository to HACS**

   - Open Home Assistant.
   - Go to `HACS` > `Integrations`.
   - Click on the three dots in the top right corner and select `Custom repositories`.
   - Add the URL of this repository (`https://github.com/obhy/home-assistant-kroncongwa`) and select `Integration` as the category.
   - Click `Add`.

2. **Install the Integration**

   - After adding the repository, find the `KroncongWA` integration in HACS.
   - Click `Install`.

3. **Configuration**

   Add the following configuration to your `configuration.yaml`:

   ```yaml
   notify:
     - name: send_wa
       platform: kroncongwa
       api_key: "your api key"
       sender: "your phone number with country code prefix, e.g. 62888xxxx"
   ```

4. **Restart Home Assistant**

   Restart Home Assistant to apply the changes.

## Usage

To send a message via KroncongWA, you can use the `notify.send_wa` service. Here is an example service call to send a simple message:

```yaml
service: notify.send_wa
data:
  message: "Hello from Home Assistant!"
  target:
    - "62811xxxxxxx"
```

Replace `"62811xxxxxxx"` with the recipient's phone number.

## Example Automation

Here is an example automation to send a message every day at 5 PM:

```yaml
automation:
  - alias: Send Daily Message
    trigger:
      - platform: time
        at: "17:00:00"
    action:
      - service: notify.send_wa
        data:
          message: "Daily reminder from Home Assistant"
          target:
            - "62811xxxxxxx"
```

Replace `"62811xxxxxxx"` with the recipient's phone number.

## License

This project is licensed under the MIT License.
```

Dengan `README.md` ini, pengguna akan memiliki panduan yang jelas tentang cara menginstal dan menggunakan integrasi KroncongWA di Home Assistant melalui HACS. Jika ada perubahan atau penambahan lainnya yang diperlukan, silakan beri tahu saya.
