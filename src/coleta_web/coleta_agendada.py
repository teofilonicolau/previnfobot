import schedule
import time
import subprocess

def tarefa():
    print("⏱️ Executando coleta automática...")
    subprocess.run(["python", "src/coleta_web/coleta_normas_inss.py"])

# Agendar para rodar toda segunda-feira às 10h
schedule.every().monday.at("10:00").do(tarefa)

while True:
    schedule.run_pending()
    time.sleep(60)
