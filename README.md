# 🫀 AppSalud

Aplicación móvil desarrollada con **KivyMD** para la estimación básica del riesgo cardiovascular a partir de datos personales y médicos.

---

## 🚀 Características

* Registro e inicio de sesión de usuarios
* Ingreso de datos personales
* Ingreso de datos médicos
* Cálculo de riesgo (Bajo, Medio, Alto)
* Interfaz estilo aplicación móvil

---

## 🧠 Variables evaluadas

* Edad
* Presión arterial
* Colesterol
* Glucosa
* Consumo de tabaco

---

## 🛠️ Tecnologías

* Python 3.11
* Kivy
* KivyMD
* JSON

---

## ▶️ Ejecutar en PC

```bash
pip install kivy kivymd
python app.py
```

---

## 📦 Generar APK (sin instalar nada en PC)

Este proyecto puede convertirse en APK usando **GitHub Codespaces**.

### Pasos rápidos:

```bash
# instalar dependencias
sudo apt update
sudo apt install -y python3-pip git zip unzip openjdk-17-jdk
pip3 install buildozer

# inicializar
buildozer init

# generar apk
buildozer -v android debug
```

El APK se genera en:

```
bin/appsalud-0.1-debug.apk
```

---

## 📱 Instalación en Android

1. Transferir el APK al celular
2. Activar "Fuentes desconocidas"
3. Instalar

---

## ⚠️ Nota

Este proyecto es académico.
No reemplaza diagnóstico médico.

---

## 👨‍💻 Autor

Jhon Stiven Calle Cabiativa
