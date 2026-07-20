import smtplib
from email.message import EmailMessage

from config import EMAIL, EMAIL_PASSWORD


def send_test_email(receiver_email):
    """
    Sends a test email to verify email configuration.
    """

    msg = EmailMessage()

    msg["Subject"] = "SmartAttend Test Email"

    msg["From"] = EMAIL

    msg["To"] = receiver_email

    msg.set_content("""
Hello,

This is a test email sent from SmartAttend.

If you received this email, the email service is working correctly.

Regards,
SmartAttend AI Attendance System
""")

    try:

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(EMAIL, EMAIL_PASSWORD)

            smtp.send_message(msg)

        return True

    except Exception as e:

        return str(e)


def send_monthly_report(
    receiver_email,
    student_name,
    report,
    month,
    year
):
    """
    Sends a monthly attendance report to a student.
    """

    msg = EmailMessage()

    msg["Subject"] = f"SmartAttend Monthly Attendance Report - {month}/{year}"

    msg["From"] = EMAIL

    msg["To"] = receiver_email

    html = f"""
    <html>
    <body style="font-family:Arial;background:#f4f4f4;padding:20px;">

        <div style="
            max-width:600px;
            margin:auto;
            background:white;
            padding:30px;
            border-radius:12px;
            box-shadow:0 0 10px rgba(0,0,0,0.1);
        ">

            <h2 style="color:#2563EB;">
                🎓 SmartAttend
            </h2>

            <h3>
                Monthly Attendance Report
            </h3>

            <hr>

            <p>Hello <b>{student_name}</b>,</p>

            <p>
                Here is your attendance report for
                <b>{month}/{year}</b>.
            </p>

            <table
                style="
                    width:100%;
                    border-collapse:collapse;
                    margin-top:20px;
                "
            >

                <tr>
                    <td><b>Present Days</b></td>
                    <td>{report['present_days']}</td>
                </tr>

                <tr>
                    <td><b>Working Days</b></td>
                    <td>{report['total_days']}</td>
                </tr>

                <tr>
                    <td><b>Attendance</b></td>
                    <td>{report['percentage']}%</td>
                </tr>

            </table>

            <br>

            <hr>

            <p>
                This report was generated automatically by
                <b>SmartAttend AI Attendance System</b>.
            </p>

            <p>
                Have a great day!
            </p>

        </div>

    </body>
    </html>
    """

    msg.add_alternative(html, subtype="html")

    try:

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(EMAIL, EMAIL_PASSWORD)

            smtp.send_message(msg)

        return True

    except Exception as e:

        return str(e)