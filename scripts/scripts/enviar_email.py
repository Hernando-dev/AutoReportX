import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

def criar_corpo_email():
    return """
    <html>
      <body style="font-family: Arial, sans-serif; line-height: 1.6; background-color: #f9f9f9; padding: 20px;">
        <div style="max-width: 600px; margin: auto; background-color: #ffffff; border-radius: 8px; padding: 30px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
          <h2 style="color: #2c3e50;">📁 Relatório Automático Atualizado</h2>
          <p>Os dados foram atualizados com sucesso.</p>
          <p>O arquivo CSV e o gráfico de tendências estão em anexo.</p>
          <hr>
          <p style="font-size: 0.9em; color: #777;">Este é um e-mail automático gerado por GitHub Actions.</p>
        </div>
      </body>
    </html>
    """

def enviar_email_para_multiplos_destinatarios():
    api_key = os.getenv("SENDGRID_API_KEY")
    emails_str = os.getenv("NOTIFY_EMAILS", "").strip()

    if not api_key or not emails_str:
        print("Variáveis de ambiente ausentes.")
        return

    destinatarios = [email.strip() for email in emails_str.split(",") if email.strip()]

    try:
        with open("dados/dados_atualizados.csv", "rb") as f:
            csv_data = f.read()
        encoded_csv = base64.b64encode(csv_data).decode()

        with open("dados/grafico_tendencia.png", "rb") as f:
            png_data = f.read()
        encoded_png = base64.b64encode(png_data).decode()

        for destinatario in destinatarios:
            message = Mail(
                from_email='github-actions@example.com',
                to_emails=destinatario,
                subject='📁 Dados atualizados - Relatório Automático',
                html_content=criar_corpo_email()
            )

            # Anexo CSV
            attachment_csv = Attachment()
            attachment_csv.file_content = FileContent(encoded_csv)
            attachment_csv.file_type = FileType('text/csv')
            attachment_csv.file_name = FileName('dados_atualizados.csv')
            attachment_csv.disposition = Disposition('attachment')
            message.attachment = attachment_csv

            # Anexo Gráfico
            attachment_png = Attachment()
            attachment_png.file_content = FileContent(encoded_png)
            attachment_png.file_type = FileType('image/png')
            attachment_png.file_name = FileName('grafico_tendencia.png')
            attachment_png.disposition = Disposition('attachment')
            message.attachment = attachment_png

            sg = SendGridAPIClient(api_key)
            response = sg.send(message)
            print(f"E-mail enviado para {destinatario} com status: {response.status_code}")

    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

if __name__ == "__main__":
    enviar_email_para_multiplos_destinatarios()
