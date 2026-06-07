from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = "8816888591:AAGzeF5r7AU4Asg2h07tfR1h44lzhZnQTDQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Order Akun", callback_data="order")],
        [
            InlineKeyboardButton("📦 Pesanan Aktif", callback_data="pesanan"),
            InlineKeyboardButton("💰 Topup Saldo", callback_data="topup")
        ],
        [
            InlineKeyboardButton("📅 Riwayat", callback_data="riwayat"),
            InlineKeyboardButton("📖 Instruksi", callback_data="instruksi")
        ],
        [InlineKeyboardButton("🎁 Klaim Voucher", callback_data="voucher")]
    ]

    teks = f"""
🏪 PUSAT JUAL AKUN TELEGRAM

Halo, {update.effective_user.first_name}

💰 Saldo Anda: Rp 0

Selamat datang di layanan transaksi akun Telegram otomatis.
"""

    await update.message.reply_text(
        teks,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def tombol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "order":
        keyboard = [
            [InlineKeyboardButton("ID 6D (50) - Rp25.000", callback_data="beli1")],
            [InlineKeyboardButton("ID 7D (60) - Rp28.000", callback_data="beli2")],
            [InlineKeyboardButton("ID 8D (70) - Rp30.000", callback_data="beli3")],
            [InlineKeyboardButton("ID 9D (75) - Rp35.000", callback_data="beli4")],
            [InlineKeyboardButton("⬅️ Kembali", callback_data="menu")]
        ]

        await query.edit_message_text(
            "🚀 PILIH PRODUK",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "menu":
        keyboard = [
            [InlineKeyboardButton("🚀 Order Akun", callback_data="order")],
            [
                InlineKeyboardButton("📦 Pesanan Aktif", callback_data="pesanan"),
                InlineKeyboardButton("💰 Topup Saldo", callback_data="topup")
            ],
            [
                InlineKeyboardButton("📅 Riwayat", callback_data="riwayat"),
                InlineKeyboardButton("📖 Instruksi", callback_data="instruksi")
            ],
            [InlineKeyboardButton("🎁 Klaim Voucher", callback_data="voucher")]
        ]

        await query.edit_message_text(
            "🏪 Menu Utama\n💰 Saldo Anda: Rp 0",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "topup":
        await query.edit_message_text(
            "💰 Topup Saldo\n\nHubungi admin atau integrasikan QRIS."
        )

    elif query.data == "riwayat":
        await query.edit_message_text(
            "📅 Belum ada riwayat transaksi."
        )

    elif query.data == "pesanan":
        await query.edit_message_text(
            "📦 Tidak ada pesanan aktif."
        )

    elif query.data == "instruksi":
        await query.edit_message_text(
            "📖 Instruksi penggunaan bot."
        )

    elif query.data == "voucher":
        await query.edit_message_text(
            "🎁 Masukkan kode voucher melalui fitur voucher."
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(tombol))

app.run_polling()
