import time
import requests
import schedule
import json
import logging
from datetime import datetime

# Registro de actividad: verás en la consola cuándo se envían los avisos
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def cargar_config():
    """Carga de forma segura el Token y los IDs desde el JSON."""
    with open('config.json', 'r') as f:
        return json.load(f)

def enviar_telegram(mensaje):
    """Lógica para repartir los mensajes a los comensales configurados."""
    config = cargar_config()
    url = f"https://api.telegram.org/bot{config['token']}/sendMessage"
    
    for chat_id in config['chat_ids']:
        try:
            requests.post(url, data={'chat_id': chat_id, 'text': mensaje})
            logging.info(f"✅ Notificación enviada con éxito.")
        except Exception as e:
            logging.error(f"❌ Error de conexión al enviar: {e}")

def aviso_comida_pau():
    """Recordatorio diario para el Frenchie."""
    enviar_telegram("🚨 ¡EL BEBÉ TIENE HAMBRE! 🐾 Hora de comer. ¡Dale su ración!")

def cuentas_del_mes():
    """Calcula y envía el desglose de facturas cada día 30."""
    if datetime.now().day == 30:
        config = cargar_config()
        gastos = config['gastos']
        total = sum(gastos.values())
        por_persona = total / 2
        
        mensaje = (
            f"🏠 --- CUENTAS DEL HOGAR --- \n\n"
            f"💰 Alquiler: {gastos['alquiler']}€\n"
            f"📱 Vodafone: {gastos['vodafone']}€\n"
            f"🎮 Nintendo: {gastos['nintendo']}€\n"
            f"💡 Luz y Gas: {gastos['luz_y_gas']}€\n"
            f"---------------------------\n"
            f"📉 TOTAL: {total}€\n"
            f"👥 TU PARTE (50%): {por_persona:.2f}€\n\n"
            f"💸 ¡ES HORA DE PAGAR, EVITA RECARGOS! 💸"
        )
        enviar_telegram(mensaje)

# --- PROGRAMACIÓN DE LA "COMANDA" ---
# Comida de Pau: 14:30 y 22:30 todos los días
schedule.every().day.at("14:30").do(aviso_comida_pau)
schedule.every().day.at("22:30").do(aviso_comida_pau)

# Revisión de facturas: 10:00 AM cada mañana (solo disparará el día 30)
schedule.every().day.at("10:00").do(cuentas_del_mes)

logging.info("🚀 Operación Casa iniciada. El bot está de guardia...")

# Bucle infinito para que el script no se cierre
while True:
    schedule.run_pending()
    time.sleep(60)