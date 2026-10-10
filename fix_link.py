with open("sleep.py", "r", encoding="utf-8") as f: code = f.read()
target_form = "https://google.com"
code = code.replace("https://forms.gle", target_form)
# На случай, если ссылка уже была частично заменена на кривой адрес:
code = re.sub(r'👉 https://docs\.google\.com/forms/d/e/[^\n]+', f'👉 {target_form}', code) if 're' in locals() else code
with open("sleep.py", "w", encoding="utf-8") as f: f.write(code)
