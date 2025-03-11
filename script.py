from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 🚀 Configuración de Selenium con Chrome en GitHub Actions
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Modo sin interfaz gráfica
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/google-chrome"  # Asegurar la ubicación correcta

# Crear WebDriver
driver = webdriver.Chrome(options=options)

# 🚀 URL del formulario y respuesta deseada
FORM_URL = "https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAN__hN8LldUNUM1WEI0ODBBMVY5MlJEMlNDTExLU1ZYVi4u"  # ⚠ REEMPLAZAR con la URL real
RESPUESTA_DESEADA = "Santiago Lucarelli"  # ⚠ REEMPLAZAR con la opción exacta

# Abrir el formulario
driver.get(FORM_URL)
time.sleep(5)  # Esperar a que cargue

# 🚀 Verificar si el formulario está en un iframe
if driver.find_elements(By.TAG_NAME, "iframe"):
    print("⚠ El formulario está dentro de un iframe. Cambiando al contexto del iframe.")
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

# 🚀 Seleccionar la opción correcta
try:
    opcion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[@aria-label='{RESPUESTA_DESEADA}']"))
    )
    opcion.click()
    print(f"✅ Se seleccionó la opción: {RESPUESTA_DESEADA}")
except Exception as e:
    print(f"⚠ No se encontró la opción: {RESPUESTA_DESEADA}. Error: {e}")

# 🚀 Encontrar el botón de "Enviar"
try:
    boton_enviar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-automation-id='submitButton']"))
    )
    boton_enviar.click()
    print("✅ Formulario enviado correctamente.")
except Exception as e:
    print(f"⚠ No se encontró el botón de envío. Error: {e}")

# Cerrar navegador
driver.quit()
