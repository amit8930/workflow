    # Check if triggered manually via GitHub Actions ("workflow_dispatch")
    is_manual_test = os.getenv("GITHUB_EVENT_NAME") == "workflow_dispatch"

    if not is_manual_test and not (now.hour == 9 and 15 <= now.minute <= 45):
        print(f"[{now.strftime('%H:%M')} IST] Outside 9:15 - 9:45 AM IST window. Skipping.")
        return

    # If running a manual test outside market hours, send a test Telegram ping
    if is_manual_test:
        send_telegram_alert(
            f"✅ *GitHub Test Successful ({now.strftime('%H:%M')} IST)*\n"
            f"• GitHub Actions & Telegram Bot are connected properly!\n"
            f"• Sample Signal Format:\n"
            f"• *Contract:* BUY 63600 PE (ATM Put)\n"
            f"• *Entry:* Above ₹385 | *Target 1:* ₹480 | *SL:* ₹310"
        )
        print("Manual test alert sent to Telegram.")
        return
