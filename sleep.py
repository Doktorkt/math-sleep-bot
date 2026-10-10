import telebot, datetime, os, re; from telebot import types
bot = telebot.TeleBot("8959639975:AAEl4U1_it8zYpV24vT-1N9omKhpryjrpDU"); u = {}
ADMIN_ID = 5161013318; HISTORY_FILE = "sleep_history.txt"
L = {
    "ru": {
        "w": "👋 Привет! Я твой ИИ-советник и дневник сказок.\n\n🌐 Выбрать язык: /lang\nℹ️ О проекте: /about\n📖 История: /history\n📊 Статистика: /stats\n🧹 Очистить: /clear\n🆘 Поддержка: /support текст\n💬 Отзывы: /reviews\n📦 Код: /code\n\nВо сколько ты ложишься спать?",
        "a": "🤖 *Калькулятор бодрствования v4.3.0*\n\n👑 *Автор:* Дмитрий Белошицкий\n\n🧠 Международный ИИ-помощник, дневник сна, поддержка и библиотека сказок.",
        "c": "🧹 *Ваш дневник сна успешно очищен!*",
        "r": "💬 *Отзывы нашего Сообщества!*\n\n✍️ *Оставить отзыв о сказках и калькуляторе сна руками с клавиатуры:*\n👉 https://clck.ru\n\nНажми /start",
        "se": "✍ Чтобы написать в поддержку, введи текст через пробел после команды.\nНапример:\n`/support Сломались кнопки!`",
        "so": "🚀 Твой вопрос успешно отправлен разработчику!",
        "he": "📭 Дневник пуст.", "ht": "📖 *Твой дневник сна:*\n\n",
        "se_t": "📭 Дневник пуст. Пряди хотя бы один расчёт сна!",
        "sr": "📊 *Средний сон за неделю:* `{avg:.1f} ч.` (Записей: {cnt})",
        "wq": "⏳ Принято! Во сколько ты просыпаешься?",
        "fe": "❌ Ошибка формата! Выберите время на кнопках.", "ce": "❌ Ошибка расчета!",
        "rt": "📊 *Расчет сна:*\n⏳ Время: {d:.1f} ч.\n⚡ Бодрость: {e:.1f}%\n💡 Совет: {t}\n\n💤 *Фазы сна:* \n{cycles}\n\n📖 *А пока малыш засыпает, почитайте ему сказку на ночь в вашем Сообществе!* Все рассказы ждут тебя на канале: t.me/dima_stories\n\n💬 *Оставить отзыв:* /reviews\n\nНажми /start",
        "tok": "Идеально! 🚀", "tn": "Нормально 👍"
    },
    "en": {
        "w": "👋 Hello! I am your AI sleep advisor and story diary.\n\n🌐 Language: /lang\nℹ️ About: /about\n📖 History: /history\n📊 Stats: /stats\n🧹 Clear: /clear\n🆘 Support: /support text\n💬 Reviews: /reviews\n📦 Code: /code\n\nWhat time do you go to sleep?",
        "a": "🤖 *Wakefulness Calculator v4.3.0*\n\n👑 *Author:* Dmitry Beloshitsky\n\n🧠 International AI assistant, sleep diary, support, and story library.",
        "c": "🧹 *Your sleep diary has been successfully cleared!*",
        "r": "💬 *Community Reviews!*\n\n✍️ *Leave your review here:*\n👉 https://clck.ru\n\nPress /start",
        "se": "✍ To write to support, enter text after the command.\nExample:\n`/support Buttons are broken!`",
        "so": "🚀 Sent successfully!",
        "he": "📭 Diary is empty.", "ht": "📖 *Your sleep diary:*\n\n",
        "se_t": "📭 Diary is empty. Complete at least one sleep calculation!",
        "sr": "📊 *Average sleep per week:* `{avg:.1f} hrs` (Entries: {cnt})",
        "wq": "⏳ Accepted! What time do you wake up?",
        "fe": "❌ Format error! Choose time from buttons.", "ce": "❌ Calculation error!",
        "rt": "📊 *Sleep Calculation:*\n⏳ Duration: {d:.1f} hrs\n⚡ Energy: {e:.1f}%\n💡 Advice: {t}\n\n💤 *Sleep cycles:* \n{cycles}\n\n📖 *While your baby falls asleep, read them a bedtime story in our Community!* All stories are waiting for you at: t.me/dima_stories\n\n💬 *Leave a review:* /reviews\n\nPress /start",
        "tok": "Perfect! 🚀", "tn": "Good 👍"
    },
    "cn": {
        "w": "👋 你好！我是您的人工智能睡眠顾问 и 童话日记。\n\n🌐 语言: /lang\nℹ️ 关于: /about\n📖 历史: /history\n📊 统计: /stats\n🧹 清空: /clear\n🆘 支持: /support 文本\n💬 评价: /reviews\n📦 源码: /code\n\n您几点上床睡觉？",
        "a": "🤖 *智能睡眠计算器 v4.3.0*\n\n👑 *作者:* 德米тpий Белошицкий\n\n🧠 国际人工智能助手、睡眠日记、技术支持和睡前故事库。",
        "c": "🧹 *您的睡眠日记已成功清空！*",
        "r": "💬 *社区用户评价！*\n\n✍️ *请在此处留下您的评价:*\n👉 https://clck.ru\n\n按 /start 开始",
        "se": "✍ 要联系技术支持，请在命令后输入内容。\n例如：\n`/support 按钮失效了！`",
        "so": "🚀 您的请求已成功发送！",
        "he": "📭 日记本是空的。", "ht": "📖 *您的睡眠日记:*\n\n",
        "se_t": "📭 请至少完成一次睡眠计算！",
        "sr": "📊 *本周平均睡眠时间:* `{avg:.1f} 小时` (次数: {cnt})",
        "wq": "⏳ 已收到！您几点起床？",
        "fe": "❌ 格式错误！请使用屏幕上的按钮选择时间。", "ce": "❌ 计算错误！",
        "rt": "📊 *睡眠分析报告:*\n⏳ 睡眠时长: {d:.1f} 小时\n⚡ 精神度: {e:.1f}%\n💡 建议: {t}\n\n💤 *睡眠周期:* \n{cycles}\n\n📖 *在宝宝入睡的同时，快来我们的社区给 them 读个睡前故事吧！* 所有故事都在频道：t.me/dima_stories\n\n💬 *留下您的评价:* /reviews\n\n按 /start 开始",
        "tok": "太棒了！🚀", "tn": "良好 👍"
    }
}
def g_l(cid): return u.get(cid, {}).get("lng", "ru")
kb_s = lambda: types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True).add("21:00", "21:30", "22:00", "22:30", "23:00", "23:30", "00:00", "01:00", "02:00")
kb_w = lambda: types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True).add("05:00", "05:30", "06:00", "06:30", "07:00", "07:30", "08:00", "09:00", "10:00")
@bot.message_handler(commands=["start", "help"])
def s_we(m):
    g = g_l(m.chat.id)
    if m.chat.id not in u: u[m.chat.id] = {"lng": g}
    for k in ["h","m","s","sleep"]: u[m.chat.id].pop(k, None)
    bot.send_message(m.chat.id, L[g]["w"], reply_markup=kb_s())
@bot.message_handler(commands=["lang"])
def c_la(m):
    kb = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True).add("🇷🇺 Русский", "🇬🇧 English", "🇨🇳 中文")
    bot.send_message(m.chat.id, "🌐 Choose language / Выберите язык:", reply_markup=kb)
@bot.message_handler(func=lambda m: m.text in ["🇷🇺 Русский", "🇬🇧 English", "🇨🇳 中文"])
def s_la(m):
    if m.chat.id not in u: u[m.chat.id] = {}
    u[m.chat.id]["lng"] = "ru" if "Русский" in m.text else "en" if "English" in m.text else "cn"
    bot.send_message(m.chat.id, "✅ Done! / Успешно!", reply_markup=types.ReplyKeyboardRemove())
    s_we(m)
@bot.message_handler(commands=["code"])
def s_co(m):
    try:
        with open("sleep.py", "rb") as d: bot.send_document(m.chat.id, d, caption="📦 *Code v4.3.0 Yandex Bridge*")
    except Exception as e: bot.send_message(m.chat.id, f"❌ {e}")
@bot.message_handler(commands=["about"])
def s_ab(m): bot.send_message(m.chat.id, L[g_l(m.chat.id)]["a"], parse_mode="Markdown")
@bot.message_handler(commands=["clear"])
def s_cl(m):
    if os.path.exists(HISTORY_FILE): os.remove(HISTORY_FILE)
    bot.send_message(m.chat.id, L[g_l(m.chat.id)]["c"], parse_mode="Markdown")
@bot.message_handler(commands=["reviews"])
def s_re(m): bot.send_message(m.chat.id, L[g_l(m.chat.id)]["r"], parse_mode="Markdown")
@bot.message_handler(commands=["support"])
def h_su(m):
    g = g_l(m.chat.id); q = m.text.replace("/support", "").strip()
    if not q: bot.reply_to(m, L[g]["se"], parse_mode="Markdown"); return
    bot.send_message(ADMIN_ID, f"🔔 *Support!*\n🆔 ID: {m.chat.id}\n🌐 {g.upper()}\n💬 {q}", parse_mode="Markdown")
    bot.reply_to(m, L[g]["so"])
@bot.message_handler(commands=["history"])
def s_hi(m):
    g = g_l(m.chat.id)
    if not os.path.exists(HISTORY_FILE): bot.send_message(m.chat.id, L[g]["he"]); return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f: lines = f.readlines()
    bot.send_message(m.chat.id, L[g]["ht"] + "".join(lines[-7:]), parse_mode="Markdown")
@bot.message_handler(commands=["stats"])
def s_st(m):
    g = g_l(m.chat.id)
    if not os.path.exists(HISTORY_FILE): bot.send_message(m.chat.id, L[g]["se_t"], parse_mode="Markdown"); return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f: lines = f.readlines()
    dr = []
    for l in lines[-7:]:
        ma = re.search(r"(?:Сон|Duration|睡眠时长):\s*`?([\d.]+)`?", l)
        if ma: dr.append(float(ma.group(1)))
    if dr: bot.send_message(m.chat.id, L[g]["sr"].format(avg=sum(dr)/len(dr), cnt=len(dr)), parse_mode="Markdown")
    else: bot.send_message(m.chat.id, L[g]["se_t"], parse_mode="Markdown")
@bot.message_handler(func=lambda m: m.chat.id in u and "sleep" not in u[m.chat.id])
def h_sl(m):
    if m.text.startswith("/"): return
    g = g_l(m.chat.id)
    try:
        h, m_t = map(int, m.text.split(":"))
        u[m.chat.id].update({"h": h, "m": m_t, "s": h + (m_t / 60.0), "sleep": True})
        bot.send_message(m.chat.id, L[g]["wq"], reply_markup=kb_w())
    except: bot.reply_to(m, L[g]["fe"])
@bot.message_handler(func=lambda m: m.chat.id in u and "sleep" in u[m.chat.id])
def h_wa(m):
    if m.text.startswith("/"): return
    g = g_l(m.chat.id)
    try:
        h, m_t = map(int, m.text.split(":")); x2 = h + (m_t / 60.0); x1 = u[m.chat.id]["s"]
        d = x2 - x1 if x2 >= x1 else (24 - x1) + x2
        if d < 5: e = max(0.0, d * 10); t = "Критически мало! 🚨 Состояние амёбы!" if g=="ru" else "Critically low! 🚨 Zombie mode!" if g=="en" else "极度缺乏! 🚨 僵尸模式!"
        elif d < 7: e = 40 + (d - 5) * 20; t = "Недосып 🥱 Будет тяжело" if g=="ru" else "Sleep deprivation 🥱 It will be hard" if g=="en" else "睡眠不足 🥱 会很 hard"
        elif d <= 9: e = 80 + (d - 7) * 10; t = L[g]["tok"]
        else: e = max(0.0, 100.0 - (d - 9) * 15); t = "Пересып 🥴 Тяжелая голова" if g=="ru" else "Overslept 🥴 Heavy head" if g=="en" else "睡 integration 过度 🥴 头脑昏沉"
        tday = datetime.datetime.now().strftime("%d.%m.%Y")
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"📅 *{tday}* — Сон: `{d:.1f} ч.`\n")
        cy = ["⏰ " + ((datetime.datetime(2026, 1, 1, u[m.chat.id]["h"], u[m.chat.id]["m"]) + datetime.timedelta(minutes=15) + datetime.timedelta(minutes=c * 90)).strftime("%H:%M")) for c in range(2, 7)]
        bot.send_message(m.chat.id, L[g]["rt"].format(d=d, e=e, t=t, cycles="\n".join(cy)), reply_markup=types.ReplyKeyboardRemove())
        for k in ["h","m","s","sleep"]: u[m.chat.id].pop(k, None)
    except: bot.send_message(m.chat.id, L[g]["ce"])
@bot.message_handler(func=lambda m: m.chat.id == ADMIN_ID and m.reply_to_message is not None)
def rep_u(m):
    try:
        uid = int(re.search(r"ID:\s*(\d+)", m.reply_to_message.text).group(1))
        bot.send_message(uid, f"📨 *Feedback:*\n\n{m.text}")
        bot.send_message(ADMIN_ID, "✅ Доставлено!")
    except: pass
print("--- МЕЖДУНАРОДНЫЙ БОЛИД v4.3.0 ЗАПУЩЕН НА ЯНДЕКСЕ! ---")
bot.infinity_polling()

import time
if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception as e:
            time.sleep(5)
