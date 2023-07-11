import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "XyffkUL9qrt7CCDSo2X07BbIJ8Y18Yf5"

while True:
     orig = input("Ciudad de Origen: ")
     if orig == "s":
         break
     dest = input("Ciudad de Destino: ")
     if dest == "s":
         break
     url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
     print("URL: " + (url))
     json_data = requests.get(url).json()
     json_status = json_data["info"]["statuscode"]
     if json_status == 0:
        print("Estado de la API: " + str(json_status) + " = Una llamada de ruta exitosa.\n")
        print("=============================================")
        print("Direcciones de " + (orig) + " a " + (dest))
        print("Duración del Viaje:   " + (json_data["route"]["formattedTime"]))
        print("Kilometros: " + str("{:.1f}".format((json_data["route"]["distance"])*1.61)))
        #print("Fuel Used (Gal): " + str(json_data["route"]["fuelUsed"])) ESTA VARIABLE NO EXISTE EN MAPQUEST ACTUALMENTE
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
             print((each["narrative"]) + " (" + str("{:.1f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
     elif json_status == 402:
        print("**********************************************")
        print("Código de estado: " + str(json_status) + "; Entradas de usuario no válidas para una o ambas ubicaciones.")
        print("**********************************************\n")
     elif json_status == 611:
        print("**********************************************")
        print("Código de estado: " + str(json_status) + "; Falta una entrada para una o ambas ubicaciones.")
        print("**********************************************\n")
     else:
       print("************************************************************************")
       print("Para código de estado: " + str(json_status) + "; Referirse a:")
       print("https://developer.mapquest.com/documentation/directions-api/status-codes")
       print("************************************************************************\n")
