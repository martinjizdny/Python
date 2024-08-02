Zde je zadani testu.
 
1. Nainstaluj si na svuj lokal WSO2 API manager verze 3.2.0. https://wso2.com/api-manager/previous-releases/
2. Nainstaluj si ActiveMQ a vytvor libovolnou Queue. https://activemq.apache.org/components/classic/
3. Vytvor jednoduche rest api v API manageru s resource POST.
4. Vytvor Python script ktery bude fungovat jako rest API, a jeho endpoint pouzij v API manageru.
5. Rest API bude prijmat XML jako input_payload.
6. Rest api tento payload odesle na backend do python scriptu.
8. Vytvor JSON payload s mappingem viz. attachment a priklady output payloadu.
9. Script posle payload jako zpravu do vytvorene Q v ActiveMQ. 
10. Posli vyslednou response s HTTP-SC.
11. Vytvor dalsi script ktery bude naslouchat na vytvorenou Q.
12. Vytvor CSV file dle prikladu viz. attachment.
13. Uloz CSV s filename viz. diagram s aktualni timestampou, do libovolne slozky na lokalu.
