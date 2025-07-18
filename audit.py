from flask import Flask, request, jsonify, redirect, send_file
from flask_mail import Mail, Message
from urllib.parse import quote, unquote
import pandas as pd
import os
from datetime import datetime


app = Flask(__name__)

# Configuración del servidor de correo
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='587',
    MAIL_USERNAME='customercare@ecuadordirectroses.com',
    MAIL_PASSWORD='wgseujhwyvuyifks',
    MAIL_USE_TLS=True,
   # MAIL_USE_SSL=False
)

mail = Mail(app)

EXCEL_FILE = 'auditoria_clicks.xlsx'

# Inicializar archivo Excel si no existe
def init_excel():
    if not os.path.exists(EXCEL_FILE):
        df = pd.DataFrame(columns=['name', 'email', 'clicked', 'clicked_at', 'ip'])
        df.to_excel(EXCEL_FILE, index=False)

init_excel()

@app.route('/send-audit-emails', methods=['POST'])
def send_audit_emails():
    try:
        from_email = request.json.get('from_email')
        subject = request.json.get('subject')
        emails = request.json.get('emails', [])

        if not isinstance(emails, list) or not emails:
            return jsonify({'status': 'error', 'message': 'Lista inválida'}), 400

        for entry in emails:
            name = entry.get('name', '')
            email = entry.get('mail', '')

            if not email:
                continue

            date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            link = f"https://flask-audit.onrender.com/track-click/{quote(email)}?name={quote(name)}"

            html = generate_pdf_html(name, date, link)

            msg = Message(
                subject=subject,
                sender=from_email,
                recipients=[email],
                html=html
            )
            mail.send(msg)

        return jsonify({'status': 'success', 'message': 'Correos enviados correctamente'}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/track-click/<email_encoded>')
def track_click(email_encoded):
    try:
        name = request.args.get('name')
        email = unquote(email_encoded)
        ip = request.remote_addr
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Cargar archivo Excel existente o crear uno nuevo si no existe
        if os.path.exists(EXCEL_FILE):
            df = pd.read_excel(EXCEL_FILE)
        else:
            df = pd.DataFrame(columns=['name', 'email', 'clicked', 'clicked_at', 'ip', 'click_count'])

        # Calcular nuevo conteo de clics para ese email
        previous_clicks = df[df['email'] == email]
        click_count = len(previous_clicks) + 1

        # Crear nueva fila con el nuevo clic
        new_row = {
            'name': name,
            'email': email,
            'clicked': 'yes',
            'clicked_at': timestamp,
            'ip': ip,
            'click_count': click_count
        }

        # Agregar la nueva fila
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        # Guardar el archivo actualizado
        df.to_excel(EXCEL_FILE, index=False)

        # Redirigir al destino deseado
        return redirect("https://www.pichincha.com/")

    except Exception as e:
        return f"Error: {e}", 500




@app.route('/download-excel')
def download_excel():
    try:
        return send_file(EXCEL_FILE, as_attachment=True)
    except FileNotFoundError:
        return "Archivo no encontrado", 404

def generate_pdf_html(name, date ,link):
    # Generar el HTML para el PDF

    html = f"""
                <div id=":1bb" class="ii gt"
    jslog="20277; u014N:xr6bB; 1:WyIjdGhyZWFkLWY6MTgzNjEyNjQzNTgxNTE1MDk3OSJd; 4:WyIjbXNnLWY6MTgzNjEyNjQzNTgxNTE1MDk3OSIsbnVsbCxudWxsLG51bGwsMSwwLFsxLDAsMF0sMjA0LDEzOTIsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLDEsbnVsbCxudWxsLFszXSxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCwwLDBd">
    <div id=":1ba" class="a3s aiL ">
        <div class="adM"> </div><u></u>
        <div>

            <table width="100%" bgcolor="#F2F2F2" cellpadding="0" cellspacing="0" border="0"
                id="m_-5243277913046183949backgroundTable">
                <tbody>
                    <tr>
                        <td>
                            <table width="550" cellpadding="0" cellspacing="0" border="0" align="center">
                                <tbody>
                                    <tr>
                                        <td width="100%">
                                            <table width="550" align="center" cellspacing="0" cellpadding="0"
                                                border="0">
                                                <tbody>
                                                    <tr>

                                                        <td align="center">
                                                            <div>
                                                                <a><img width="550" border="0" height="114" alt=""
                                                                        style="display:block;border:none;outline:none;text-decoration:none"
                                                                        src="https://ci3.googleusercontent.com/meips/ADKq_NZgVdiZmQw6kg_-eztk6lpKi1LkdZCmcBvcp6j7CYVIyYrGPELETYuh6R6481bnwpOv9sC3khXxrCmQBiG3hZmAIjOh1u-wjIApm5tVo6Kwvw=s0-d-e1-ft#http://wwwh1.pichincha.com/pichincha/omni/images/header.png"
                                                                        class="CToWUd" data-bit="iit"></a>
                                                            </div>
                                                        </td>

                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>




            <table width="100%" bgcolor="#F2F2F2" cellpadding="0" cellspacing="0" border="0"
                id="m_-5243277913046183949backgroundTable">
                <tbody>
                    <tr>
                        <td>
                            <table width="550" cellpadding="0" cellspacing="0" border="0" align="center">
                                <tbody>
                                    <tr>
                                        <td width="100%" bgcolor="#f6f4f5" style="padding:20px">
                                            <table width="510" align="center" cellspacing="0" cellpadding="0"
                                                border="0">
                                                <tbody>
                                                    <tr>
                                                        <td align="left" bgcolor="#ffffff"
                                                            style="font-family:Arial,sans-serif;color:#333333;font-size:12px;padding-top:30px;padding-right:30px;padding-left:30px;padding-bottom:20px;text-align:left;line-height:22px">
                                                            <strong>{date}</strong>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td align="left" bgcolor="#ffffff"
                                                            style="font-family:Arial,sans-serif;color:#333333;font-size:12px;padding-top:0px;padding-right:30px;padding-left:30px;padding-bottom:0px;text-align:center;line-height:22px">
                                                            <strong>Banca Movil</strong>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td align="left" bgcolor="#ffffff"
                                                            style="font-family:Arial,sans-serif;color:#333333;font-size:12px;padding-top:20px;padding-right:30px;padding-left:30px;padding-bottom:20px;text-align:left;line-height:16px">
                                                            <strong>{name}</strong>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td align="left" bgcolor="#ffffff"
                                                            style="font-family:Arial,sans-serif;color:#333333;font-size:12px;padding-top:10px;padding-right:30px;padding-left:30px;padding-bottom:20px;text-align:left;line-height:16px">
                                                            Tu consumo se realizó con éxito.</td>
                                                    </tr>

                                                    <tr>
                                                        <td align="left" bgcolor="#ffffff"
                                                            style="font-family:Arial,sans-serif;color:#333333;font-size:12px;padding-top:0px;padding-right:30px;padding-left:30px;padding-bottom:0px;text-align:left;line-height:22px">
                                                            <table align="center" border="0" cellpadding="0"
                                                                cellspacing="0"
                                                                style="border-collapse:collapse;border:1px solid #f6f4f5"
                                                                width="440">
                                                                <tbody>
                                                                    <tr>
                                                                        <td colspan="2" align="left" bgcolor="#f6f4f5"
                                                                            style="font-family:Arial,sans-serif;color:#333333;font-size:12px;padding-top:10px;padding-right:40px;padding-left:40px;padding-bottom:10px;text-align:center;line-height:16px">
                                                                            <strong>Detalle
                                                                            </strong>
                                                                        </td>
                                                                    </tr>

                                                                    <tr>
                                                                        <td width="40%" align="right" bgcolor="#ffffff"
                                                                            style="font-family:Arial,sans-serif;color:#333333;font-size:12px;padding-top:20px;padding-right:3px;padding-left:20px;padding-bottom:5px;text-align:left;line-height:16px">
                                                                            <strong>IP:</strong>
                                                                        </td>

                                                                        <td width="60%" align="left" bgcolor="#ffffff"
                                                                            style="font-family:Arial,sans-serif;color:#333333;font-size:12px;padding-top:20px;padding-right:3px;padding-left:3px;padding-bottom:5px;text-align:left;line-height:16px">
                                                                            2800:430:1384:1760:1bd8:32e4:<wbr>88e6:f554
                                                                        </td>
                                                                    </tr>
                                                                    <tr>
                                                                        <td width="40%" align="right" bgcolor="#ffffff"
                                                                            style="font-family:Arial,sans-serif;color:#333333;font-size:12px;padding-top:5px;padding-right:3px;padding-left:20px;padding-bottom:5px;text-align:left;line-height:16px">
                                                                            <strong>Ubicación:</strong>
                                                                        </td>

                                                                        <td width="60%" align="left" bgcolor="#ffffff"
                                                                            style="font-family:Arial,sans-serif;color:#333333;font-size:12px;padding-top:5px;padding-right:3px;padding-left:3px;padding-bottom:5px;text-align:left;line-height:16px">
                                                                            Ecuador</td>
                                                                    </tr>

                                                                </tbody>
                                                            </table>
                                                        </td>
                                                    </tr>

                                                    <tr>
                                                        <td align="left" bgcolor="#ffffff"
                                                            style="font-family:Arial,sans-serif;color:#333333;font-size:12px;padding-top:30px;padding-right:30px;padding-left:30px;padding-bottom:0px;text-align:left;line-height:16px">
                                                            Ver también: <a href="{link}">Detalle de su consumo</a>
                                                    </tr>
                                                    <tr>
                                                        <td align="left" bgcolor="#ffffff"
                                                            style="font-family:Arial,sans-serif;color:#333333;font-size:12px;padding-top:20px;padding-right:30px;padding-left:30px;padding-bottom:40px;text-align:justify;line-height:16px">
                                                            Si no has solicitado este
                                                            servicio, repórtalo a nuestra Banca Telefónica al
                                                            &nbsp;<br><a href="{link}">1800 0000 0000.</a><br><br>
                                                            Gracias por utilizar
                                                            nuestros servicios. <br><br> Atentamente,<br> <strong>Banco
                                                                Pichincha</strong>
                                                        </td>

                                                    </tr>
                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>



            <table width="100%" bgcolor="#F2F2F2" cellpadding="0" cellspacing="0" border="0"
                id="m_-5243277913046183949backgroundTable">
                <tbody>
                    <tr>
                        <td>
                            <table width="550" cellpadding="0" cellspacing="0" border="0" align="center">
                                <tbody>
                                    <tr>
                                        <td width="100%">
                                            <table bgcolor="#0F265C" width="550" cellpadding="0" cellspacing="0"
                                                border="0" align="center">
                                                <tbody>

                                                    <tr>
                                                        <td align="center">
                                                            <div>
                                                                <a><img width="550" border="0" alt=""
                                                                        style="display:block;border:none;outline:none;text-decoration:none"
                                                                        src="https://ci3.googleusercontent.com/meips/ADKq_NbAooAdBwCK1uNHveVCT-3z4lZfw26zLNxUEF-R2L613QDTv8JC3Pls2ZflNOd2ph_IY_5v1VPBL_nnSWDZgdZxXWgqXKCI35kdkFK854B1jeTxUIlr=s0-d-e1-ft#https://wwwh1.pichincha.com/pichincha/omni/images/footer_550.png"
                                                                        class="CToWUd a6T" data-bit="iit" tabindex="0">
                                                                    <div class="a6S" dir="ltr"
                                                                        style="opacity: 0.01; left: 574px; top: 789px;">
                                                                        <span data-is-tooltip-wrapper="true" class="a5q"
                                                                            jsaction="JIbuQc:.CLIENT"><button
                                                                                class="VYBDae-JX-I VYBDae-JX-I-ql-ay5-ays CgzRE"
                                                                                jscontroller="PIVayb"
                                                                                jsaction="click:h5M12e; clickmod:h5M12e;pointerdown:FEiYhc;pointerup:mF5Elf;pointerenter:EX0mI;pointerleave:vpvbp;pointercancel:xyn4sd;contextmenu:xexox;focus:h06R8; blur:zjh6rb;mlnRJb:fLiPzd;"
                                                                                data-idom-class="CgzRE"
                                                                                data-use-native-focus-logic="true"
                                                                                jsname="hRZeKc"
                                                                                aria-label="Descargar el archivo adjunto "
                                                                                data-tooltip-enabled="true"
                                                                                data-tooltip-id="tt-c113"
                                                                                data-tooltip-classes="AZPksf" id=""
                                                                                jslog="91252; u014N:cOuCgd,Kr2w4b,xr6bB; 4:WyIjbXNnLWY6MTgzNjEyNjQzNTgxNTE1MDk3OSJd; 43:WyJpbWFnZS9qcGVnIl0."><span
                                                                                    class="OiePBf-zPjgPe VYBDae-JX-UHGRz"></span><span
                                                                                    class="bHC-Q" jscontroller="LBaJxb"
                                                                                    jsname="m9ZlFb" soy-skip=""
                                                                                    ssk="6:RWVI5c"></span><span
                                                                                    class="VYBDae-JX-ank-Rtc0Jf"
                                                                                    jsname="S5tZuc"
                                                                                    aria-hidden="true"><span
                                                                                        class="notranslate bzc-ank"
                                                                                        aria-hidden="true"><svg
                                                                                            viewBox="0 -960 960 960"
                                                                                            height="20" width="20"
                                                                                            focusable="false"
                                                                                            class=" aoH">
                                                                                            <path
                                                                                                d="M480-336L288-528l51-51L444-474V-816h72v342L621-579l51,51L480-336ZM263.72-192Q234-192 213-213.15T192-264v-72h72v72H696v-72h72v72q0,29.7-21.16,50.85T695.96-192H263.72Z">
                                                                                            </path>
                                                                                        </svg></span></span>
                                                                                <div class="VYBDae-JX-ano"></div>
                                                                            </button>
                                                                            <div class="ne2Ple-oshW8e-J9" id="tt-c113"
                                                                                role="tooltip" aria-hidden="true">
                                                                                Descargar</div>
                                                                        </span>
                                                                    </div>
                                                                </a>
                                                            </div>
                                                        </td>
                                                    </tr>

                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>


            <table width="100%" bgcolor="#F2F2F2" cellpadding="0" cellspacing="0" border="0"
                id="m_-5243277913046183949backgroundTable">
                <tbody>
                    <tr>
                        <td>
                            <table width="550" cellpadding="0" cellspacing="0" border="0" align="center">
                                <tbody>
                                    <tr>
                                        <td width="100%">
                                            <table bgcolor="#F2F2F2" width="550" cellpadding="0" cellspacing="0"
                                                border="0" align="center">
                                                <tbody>

                                                    <tr>
                                                        <td width="100%" height="10"></td>
                                                    </tr>

                                                    <tr>
                                                        <td bgcolor="#f6f4f5"
                                                            style="padding:10px 30px;font-family:Arial,sans-serif;color:#67554f;font-size:9px;padding-top:10px;padding-right:10px;padding-left:10px;padding-bottom:10px;text-align:justify;line-height:10px">
                                                            <strong>Nota de
                                                                descargo:&nbsp;</strong>La información contenida en este
                                                            e-mail es confidencial y sólo puede ser
                                                            utilizada por el individuo o la compañía a la
                                                            cual está dirigido.&nbsp;Esta información
                                                            no debe ser distribuida ni copiada total o parcialmente por
                                                            ningún medio sin la autorización del BANCO
                                                            PICHINCHA C.A.<br>La organización no
                                                            asume responsabilidad sobre información,
                                                            opiniones o criterios contenidos en este e-mail que no
                                                            esté relacionada con negocios oficiales de nuestra
                                                            institución.<br>Banco Pichincha nunca
                                                            solicita información financiera ni claves
                                                            vía telefónica, correos
                                                            electrónicos o redes sociales.<br>
                                                            <strong>Disclaimer:&nbsp;</strong>The
                                                            information contained in this e-mail is confidential
                                                            and intended only for the use of the person or company to
                                                            which it is addressed.&nbsp;This information is
                                                            considered provisional and referential; it cannot be
                                                            totally or partially distributed or copied by any media
                                                            without the authorization from BANCO PICHINCHA
                                                            C.A.<br>The Bank does not assume
                                                            responsibility about this information, opinions or
                                                            criteria contented in this e-mail.
                                                        </td>
                                                    </tr>

                                                    <tr>
                                                        <td width="100%" height="10"></td>
                                                    </tr>

                                                </tbody>
                                            </table>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </td>
                    </tr>
                </tbody>
            </table>
            <div class="yj6qo"></div>
            <div class="adL">



            </div>
        </div>
        <div class="adL">
        </div>
    </div>
</div>
            """

    return html



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

