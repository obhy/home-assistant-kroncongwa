```markdown
# Home Assistant KroncongWA Integration

Send Home Assistant notifications to WhatsApp using KroncongWA (http://notify.obhy.net).

## Installation

1. **Create the Directory**

   Create a directory called `kroncongwa` in the `custom_components` directory of your Home Assistant configuration.

   ```sh
   mkdir -p custom_components/kroncongwa
   ```

2. **Copy Files**

   Copy the following files into the `kroncongwa` directory:

   - `__init__.py`
   - `manifest.json`
   - `notify.py`

   The structure should look like this:

   ```
   custom_components/kroncongwa/
   ├── __init__.py
   ├── manifest.json
   └── notify.py
   ```

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

Dengan file `README.md` ini, pengguna akan memiliki panduan yang jelas tentang cara menginstal dan menggunakan integrasi KroncongWA di Home Assistant. Jika ada perubahan atau penambahan yang diperlukan, silakan beri tahu saya.
