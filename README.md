# AutoReportX
# Relatório Automático com Python e GitHub Actions

Este repositório contém uma automação completa para:
- Baixar/Atualizar dados CSV
- Aplicar transformações com SQL
- Gerar histórico de relatórios
- Criar gráficos de tendência
- Enviar e-mails automatizados com anexos
- Agendamento via GitHub Actions

## Funcionalidades

- ✅ Atualização de hora em hora
- ✅ Histórico versionado dos dados
- ✅ Gráficos de linha com matplotlib
- ✅ E-mails com anexos (CSV e PNG)
- ✅ Múltiplos destinatários
- ✅ Notificação apenas em caso de erro

## Como usar

1. Configure os secrets no GitHub:
   - `SENDGRID_API_KEY`: Sua chave do SendGrid
   - `NOTIFY_EMAILS`: Lista de e-mails separados por vírgula

2. O script roda automaticamente de hora em hora.
