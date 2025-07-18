import os import random from telegram import Update, ReplyKeyboardMarkup from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

levels = { "Лайт": [ "Сними одну вещь одежды.", "Нежно поцелуй партнёра в шею.", "Сделай партнёру массаж спины 2 минуты.", "Прошепчи партнёру на ухо, что ты с ним сделаешь позже.", "Оближи партнёру палец, как будто это что-то неприличное.", "Сделай 3 пощёчины по попе партнёра.", "Опиши эротическую фантазию с партнёром.", "Пусть партнёр тебя нюхает с закрытыми глазами и угадывает, где.", "Поменяйтесь нижним бельём на 5 минут.", "Сделай партнёру 5 поцелуев, но ни одного в губы." ], "Средний": [ "Вставь анальную пробку и останься с ней на 10 минут.", "Поиграй с EXTREME MAGIC WAND на минимальной мощности 2 минуты.", "Партнёр вставляет виброяйцо — и управляет им 3 минуты.", "Поставь Orca на клитор и продержи 60 секунд.", "Пусть партнёр лижет соски 1 минуту, пока ты лежишь связанный(ая).", "Выбери позу и замри в ней, пока партнёр тебя дразнит.", "Оближи партнёру живот и ниже… но не трогай интимное.", "Сними всё и сядь на колени перед партнёром, смотри в глаза 30 сек.", "Дай партнёру миостимуляцию на малой мощности 2 минуты.", "Партнёр гладит твоё тело игрушкой, пока ты с завязанными глазами." ], "Жёсткий": [ "Пусть партнёр вставит дилдо на присоске в тебя — сам/сама крути тазом.", "Стимуляция EXTREME MAGIC WAND на максимум 2 минуты — без оргазма.", "Мастурбируй реалистичным мастурбатором 1 минуту перед партнёром.", "Засунь анальную пробку и выполни 10 приседаний.", "Миостимуляция током на максимуме 1 минуту.", "Сиди голым(ой), пока партнёр тебе шепчет неприличные приказы.", "Дрочи партнёру, пока он/она говорит тебе гадости.", "Оральное удовольствие — 2 минуты, по таймеру, потом остановка.", "Попробуй два устройства одновременно: вибро-яйцо + орка.", "Надень повязку и привяжи её к кровати, пока тебе будут читать новый фант." ] }

current_level = "Лайт"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): keyboard = [["/next", "/setlevel Лайт"], ["/setlevel Средний", "/setlevel Жёсткий"], ["/help"]] reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True) await update.message.reply_text( f"Привет! Я бот с фантами для постельных игр. Текущий уровень: {current_level}\nНапиши /next — и я пришлю фант!", reply_markup=reply_markup )

async def next_fant(update: Update, context: ContextTypes.DEFAULT_TYPE): fan_list = levels.get(current_level, []) if not fan_list: await update.message.reply_text("Фанты для текущего уровня не найдены.") else: await update.message.reply_text(random.choice(fan_list))

async def set_level(update: Update, context: ContextTypes.DEFAULT_TYPE): global current_level if context.args: level = " ".join(context.args) if level in levels: current_level = level await update.message.reply_text(f"Уровень установлен: {current_level}") else: await update.message.reply_text("Такой уровень не найден. Доступны: " + ", ".join(levels.keys())) else: await update.message.reply_text("Укажи уровень после команды. Пример: /setlevel Средний")

async def add_fant(update: Update, context: ContextTypes.DEFAULT_TYPE): if context.args: new_fant = " ".join(context.args) levels[current_level].append(new_fant) await update.message.reply_text(f"Фант добавлен в уровень {current_level}.") else: await update.message.reply_text("Напиши фант после команды. Пример: /addfant Лизнуть шею 3 раза")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE): help_text = ( "📜 Команды бота:\n" "/start — запустить бота и меню\n" "/next — получить случайный фант из текущего уровня\n" "/setlevel <уровень> — установить уровень (Лайт, Средний, Жёсткий)\n" "/addfant <текст фанты> — добавить свою фанту в текущий уровень\n" "/help — показать это меню" ) await update.message.reply_text(help_text)

if name == 'main': app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("next", next_fant))
app.add_handler(CommandHandler("setlevel", set_level))
app.add_handler(CommandHandler("addfant", add_fant))
app.add_handler(CommandHandler("help", help_command))

print("Бот запущен")
app.run_polling()

