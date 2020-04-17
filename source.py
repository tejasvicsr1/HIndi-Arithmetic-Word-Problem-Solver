source = []
sentences = [
    "एक वेज्ञानिक मेडिकल लेब में रक्त की जांच कर रहा था। 2 किस्सो में मिलाकर उसे 7341 रक्त कोशिकाए थी। पेहले किस्से में उन्हे 4221 कोशिकाए मिली, तो दूसरे में कितनी थी?",
    "केटी के निव्र्त्ती की कमाई हाल ही  में $ 12  से घटी है। अगर इसके पेहले उसकी कमाई में $ 1472  थे, तो अब कितने बाकी हैं?",
    "एक पेटरी डिश में वेज्ञानिक ने 600 बेकटीरिया को 8917 तक बढने दिया। अब कितने बेकटीरिया मौजूद हैं?",
    "मौली वॅफटिन्ग पाई कम्पनी की मालकिन है। आज सुबह उनके क्र्मचारियो ने 816 अंडो का इस्तमाल खाना बनाने में इस्नमाल किया। अगर सब क्र्मचारियो ने मिलकर पूरे दिन में 1339 अंडो का प्रयोग किया, तो उन्होने दोपहर को कितने अंडो का उपयोग किया?",
    "एक  किसान के 6048 में से 193 बकरे सफेद हैं और बाकी सब काले हैं। फिर उस किसान के पास कितने काले बकरे हैं?",
    "एक कम्पनी ने हैनकोक कौनटी के कुछ घरो को नीला और सफेद रंग दिया। उन्होने कुल मिलाकर 6689 पेंट के डब्बो का इस्तमाल किय। अगर उन्मे से 193 सफेद रंग के थे तो नीले रंग के कितने डिब्बे थे?",
    "सिलवर ग्रोव लाईब्ररी ने पैसे मानगकर 2647 किताबे खरीदी। अब लईब्ररी के पास कुल मिलाकर 8582 किताबे हैं। तो किताबे खरीदने के पेहले उनके पास कितनी किताबे थी?",
    "ओस्कर का घर पाठशाला से 0.75 मील दूर है और चारली का घर 0.25 मील। तो ओस्कर को चारली से बस में कितना ज़्यादा दूर बैठना होगा?",
    "कारेन ने पहले 0.25 कप अखरोट आटे में डाला। फिर उसने 0.25 कप बादाम आटे में मिलाया। कुल मिलाकर उसने आटे में कितने कप मिलाये?",
    "केनडल अपने माता-पिता के साथ गाडी चलाना सीख रही है। उसने अपनी माता के साथ 0.166 मील गाडी चलाई और अपने पिता के साथ उसने 0.5 मील गाडी चलाई। तो कुल मिलाकर उसने कितने मील गाडी चलाई?",
    "एक दरज़ी ने एक स्किर्ट से 0.75 इंच काटा और एक पेंट से 0.5 इंच। दरज़ी ने फिर स्किर्ट से कितना ज़्यादा कपडा काटा।",
    "डारनल 0.875 मील दौडा और फिर 0.75 मील चला। अंत मे डारनल कितना ज़्यादा दौडा?",
    "एल्ला के दो कुत्ते हैं। हर दिन एक कुत्ता 0.125 कप खाना खात है और दूसरा कुत्ता 0.125 कप खाना खाता है। कुल मिलाकर उन्होने कितने कप खाना खाया?",
    "ब्लेक ने बालटी में 0.8 लीटर पानी भरा । फिर उसने उसमे से 0.2 लीटर पानी निकाला । अंत में फिर बालटी में कितना पानी हैं?",
    "मोंट्या अपने महीने कि कमाई में से 60 प्र्तिश्त राशन पे खर्च करता है और 20 प्रतिशत खाने पर । कुल मिलाकर मोंट्या एक महीने में कितने प्रतिशत पैसे खर्च करता है।",
    "ओलसन के गणित क्लास्स में 0.7 प्रतिशत छात्र को 10 अंख मिले और 0.2 छात्रो को 9 अंख मिले। कुल मिलाकर कितने छात्रो को या तो 10 या तो 9 मिला।",
    "जब मिशेल डिलिवरी शुरु करने जा रही थी, तब उसके टंकी में 0.5 लीटर गैस थी। जब उसकी डिलिवरी खतम हुइ तब उसके टंकी में 0.166 लीटर बाकी था। उसने राह में कितना गैस का इस्तमाल किया।",
    "क्रेग स्कूल से डेविड के घर तक 0.2 मील चला और डेविड के घर से अपने घर तक 0.7 मील चला । कुल मिलाकर वह कितने मील चला ।",
    "ग्रेग और शेरन के खेत आस-पास है। ग्रेग ने 0.4 एकर गेहू फसल काटी और शेरन ने 0.1 एकर । ग्रेग ने शेरन से कितने ज़्यादा एकर फसल काटी । ",
    "जोनाह ने 0.3 कप पीली किशमिश और 0.4 कप काली किशमिश को एक साथ मिलाया। कुल मिलाकर उस मिश्रण में कितने कप किशमिश थे?",
    "इंगलेंड में सुबह 0.125 इंच बर्फ गिरि और शाम को 0.5 इंच । कुल मिलाकर उस दिन इंगलेंड में कितने इंच बर्फ गिरि",
    "खाना एकठ्ठा करने के दोहरान, उनहे अलग किया गया । उसमे 0.125 कप सूप था, 0.125 कप सब्ज़ी और 0.5 कप पास्ता। कुल मिलाकर कितने कप इकठ्ठा हुए। ",
    "नीना ने फुटबाल में उछ खेलने के लिये अभ्यास करना शुरु किया । उसने पहले 0.0833 मील की दौड लगाई । फिर उसने 0.0833 और 0.666 मील की दौड लगाई । कुल मिलाकर उसने कितने मील दौडे। ",
    "पिछले शनिवार रवी मोहोल्ले भर घूमकर काम कर रहा था। पहले 0.3 मील अपने घर से लैब्ररी तक चलकर उसने 0.1 मील लैब्ररी से पोस्ट औफ्फिस चला । फिर उसने पोस्ट औफ्फिस से घर तक 0.4 मील चला । कुल मिलाकर उसने कितने मील चला। ",
    "आज दोपहर क्रेग स्कूल से बस में पहले 3.8335 मील चला । फिर वह बस स्टोप से घर 0.166 मील चला। क्रेग फिर बस में,  चलने से कितने मील ज़्यादा गया । ",
    "एक दिन सैम ने पूल में 1 बकट पानी डाला । फिर उसने और 8.8 बकट पानी और डाला । कुल मिलाकर उसने कितने पानी के बकट पूल में डाले ?",
    "कैल ने पीटी के दोहरान ग्रोन्ड के 1.125 चक्कर मारे और फिर 2.125 चक्कर रेस के अभ्यास दोहरान मारे। कुल मिलाकर कैल ने ग्रोन्ड के कितने चक्कर मारे। ",
    "एक बकट में 3 लीटर पानी भरा हुआ है। अगर डेरेन ने उसमे और 6.8 लीटर पानी और डाला, तो कुल मिलाकर बकट में कितने लीटर पानी है?",
    "एक पार्टी के दोहरान मेसन और उसके दोस्तो ने 2.665 बौटल नीम्बू सोडा और 2.665 बौटल कोला पिया । कुल मिलाकर उन्होने कितने बौटल पिया ?",
    "एलेक और उसके दोस्त ने शनिवार को 3.25 कप ऐस क्रीम खाया और रविवार को 0.25 कप ऐस क्रीम खाया । तो कुल मिलाकर उन्होने कितने कप ऐस क्रीम खाये ?",
    "एक हफते मैं एमिलि का परिवार 0.5 लिटर गाय का दूध और 0.1 लिटर भैस का दूध पीता है । कुल मिलाकर वे कितने लीटर दूध पीते है?",
    "एक मछ्लि वाले ने पहले 1 मछली 0.3 फुट की पकडी और फिर 0.2 की पकडी । पहली मछली दूसरे से कितनी ज़्यादा बडी है?",
    "एक मोबाईल कमपनी के 7422 कस्तमर है। अगर 723 कस्तमर अम्रीका में रहते हैं, तो और सब जगह कितने लोग रहते है?",
    "रामू को एक खज़ाना मिला जिसमे 5155 रत्न थे। अगर उसमे से 45 हीरे थे, और बाकी सब रूबी है, तो कितने रूबी है? ",
    "एक खेल मैं पौल के 3103 पोइंट्स है। अगर वह और उसके भाई के मिलाकर 5816 पोइंट्स है, तो उसके भाई के कितने पोइंट्स है?",
    "जोआन को समुद्रतट पर 70 सीपें मिलीं । उसने सैम को अपनी कुछ सीपें दीं । उसके पास 27 सीपें हैं। उसने कितने सीपें सैम को दिए?",
    "मैरी एक केक पका रही है। रेसेपी 8 कप आटा चाहती है। उसने पहले से ही 2 कप डाल दिए। उसे कितने और कप डालने की आवश्यकता है?",
    "खलिहान में घास की 28 गांठें थीं। टिम ने खलिहान में गांठें खड़ी कर दीं आज । खलिहान में अब 54 गांठें हैं। उसने कितनी गांठें खलिहान में रखी थी ?",
    "जोआन ने इस साल 4 फुटबॉल खेल खेले। वह पिछले साल 9 खेलों में गई थी। जोआन कुल कितने फुटबॉल खेलों में गए?",
    "पार्क में वर्तमान में 4 अखरोट के पेड़ हैं। पार्क कर्मी आज 6 अखरोट के पेड़ लगाएंगे। पार्क में कितने अखरोट के पेड़ होंगे जब काम समाप्त हो जाते हैं?",
    "टिम की बिल्ली के कुछ बच्चे थे। उसने जेसिका को 3 और सारा को 6 बिल्ली के बच्चे दिए। उसके पास अब है 9 बिल्ली के बच्चे हैं। शुरुआत में उसके पास कितने बिल्ली के बच्चे थे?",
    "सारा ने 4 प्याज उगाये, सैली ने 5 प्याज उगाये और फ्रेड ने 9 प्याज उगाये। सभी में कितने प्याज उगाये?",
    "जेसन ने 23 तरबूज और 18 शलजम उगाए। नैन्सी ने 28 तरबूज उगाए। उन्होंने कुल कितने तरबूज उगाये?",
    "समुद्र तट पर टॉम को 15 सीशेल्स और फ्रेड को 43 सीशेल्स मिले। जब उन्होंने उन्हें साफ किया, तो उन्हें पता चला कि 29 टूटे थे। उन्होंने कुल कितने समुद्र-तट खोजे?",
    "सारा के पास 31 लाल और 15 हरे गुब्बारे हैं। सैंडी के पास 24 लाल गुब्बारे हैं। उनके पास कुल कितने लाल गुब्बारे हैं?",
    "मेलानी के बैंक में 19 रुपये थे। उसके पिता ने उसे 39 रुपये दिए और उसकी माँ ने उसे 25 रुपये दिए। मेलानी के पास अभी कितने रुपये हैं ?",
    "माइक की अपनी लाइब्रेरी में 35 किताबें हैं। उन्होंने सप्ताहांत में एक यार्ड बिक्री में कई किताबें खरीदीं । उसकी लाइब्रेरी में अब 56 किताबें हैं। यार्ड बिक्री पर उसने कितनी किताबें खरीदीं?",
    "बेनी को उसके जन्मदिन के लिए 67 डॉलर मिले। वह एक खेल की दुकान में गया और एक बेसबॉल दस्ताने, बेसबॉल और बल्ले खरीदा। उसके पास 33 डॉलर बचे थे, तो उसने बेसबॉल गियर पर कितना खर्च किया?",
    "टॉम को 7 सीशेल मिले लेकिन 4 टूटे हुए थे। टॉम को कितने अखंडित सीशेल मिले?",
    "एक रेस्ट्रॉन्ट ने आज दोपहर के भोजन के दौरान 6 केक परोसे और रात के खाने के दौरान 9 केक परोसे।आज कुल कितने केक परोसे गए?",
    "जोआन के पास 8 नारंगी गुब्बारे हैं लेकिन उनमें से 2 खो गए। जोआन के पास अब कितने नारंगी गुब्बारे हैं?",
    "माइक के पास 87 बेसबॉल कार्ड हैं। सैम ने माइक के 13 बेसबॉल कार्ड खरीदे। माइक के पास अब कितने बेसबॉल कार्ड हैं?",
    "जोआन ने $ 5.20 के लिए एक बास्केटबॉल गेम और $ 4.23 के लिए एक रेसिंग गेम खरीदा। जोआन ने कुल वीडियो गेम पर कितना खर्च किया?",
    "मैरी को फल खाना बहुत पसंद है। मैरी ने जामुन के लिए $ 11.08, सेब के लिए $ 14.33, और आड़ू के लिए $ 9.31 का भुगतान किया। कुल मिलाकर उसने कितने पैसे खर्च किये?",
    "एक जहाज में 5973 टन माल भरा है। यह बहामास में रुक जाता है, जहां नाविकों ने 8723 टन माल को जहाज पर चढ़ाया। कितने टन का माल अब जहाज पर है?",
    "अबे का परिवार बहामास से जापान चला गया, इसलिए वह अपने पैसे को जापानी येन में परिवर्तित किये । उनके चेकिंग खाते में 6359 येन हैं और उनके बचत खाते में 3485 येन है। उनके पास कुल कितने येन हैं?",
    "मैदान में धूल भरी आंधी चली। उससे 64535 एकड़ जमीन धूमिल हो गयी, लेकिन 522 एकड़ जमीन छूट गयी। मैदान की ज़मीन कितने एकर की है?",
    "एक बहु-राष्ट्रीय निगम में 2041 अंशकालिक कर्मचारी हैं और 63093 पूर्णकालिक कर्मचारी। निगम में कुल कितने कर्मचारी काम करते हैं ?",
    "पिछले साल, 90171 लोग एक देश में पैदा हुए और 16320 इसमें आके बस गए। कुल कितने नए लोग देश में पिछले साल रहने लगे ?",
    "क्रिस्टीना ने 69 डॉलर अपने बैंक खाते में ट्रांसफर किए। नतीजतन , खाते में अब $ 26935 है। ट्रांसफर के पहले खाते में कितने डॉलर थे ?",
    "मैरी के बगीचे में 8 आलू थे। खरगोशों ने 3 आलू को खा लिया। मैरी के पास अब कितने आलू हैं?",
    "जोआन के बैंक में 5 रुपए थे। उसने अपने 2 रुपए खर्च किए। अब उसके पास कितने रुपए हैं ?",
    "टॉम को समुद्र तट पर 5 सीशेल मिले। उसने जेसिका का 2 सीशेल दिए। अब उसके पास कितने सीशेल हैं?",
    "जेसिका के बैंक में 8 रुपए थे। उसकी बेहेन ने 3 रुपए उससे उधार लिए। अब जेसिका के पास कितने रुपए हैं?",
    "एक रेस्ट्रॉन्ट ने 9 बर्गर शाम के भोजन के लिये बनाये। केवल 3 बर्गर ही परोसे गए। कितने बर्गर भोजन के बाद बच गए।",
    "सैली के पास 27 पोकेमॉन कार्ड थे। डैन ने उसे 41 नए पोकेमॉन कार्ड दिए। सैली ने 20 पोकेमॉन कार्ड खरीदे। सैली के पास कितने पोकेमॉन कार्ड हैं ?",
    "दराज में 9 क्रेयॉन हैं। बेनी ने 3 क्रेयॉन को दराज के अंदर रखा। अब दराज में कुल कितने क्रेयॉन हैं?",
    "डायने मधुमक्खी पालक है। पिछले साल, उसकी 2479 पाउंड शहद की फसल थी । इस साल, उसने कुछ नए मधुमक्खी खरीदे और अपना शहद की फसल को 6085 पाउंड से बढ़ाया। इस साल डायने की कितनी शहद की फसल थी।",
    "घरों की बढ़ोतरी से पहले, लॉरेंस काउंटी में 1426 घर थे। अब 2000 घर हैं। बढ़ोतरी के दौरान कितने घरों का निर्माण किया गया ?",
    "एक आर्डर को पूरा करने के लिए, कारखाने ने 61921 गज हरा रेशम और 49500 गज गुलाबी रेशम को रंगा। उस आर्डर के लिए कुल कितने गज के रेशम को रंगा गया ?",
    "डैन के पास 32 हरे और 38 बैंगनी गोलियां हैं। माइक ने उससे 23 हरे गोलियां ले ली । डैन के पास कितने हरे गोलियां बची हैं?",
    "जैसन के पास 96 किताबे हैं और उसने 9 पढ़ी हैं । मेरी के पास 42 किताबे हैं । उन दोनों के पास कुल कितने किताबे हैं?",
    "दराज में 41 क्रेयॉन हैं और 25 पेंसिल । सैम ने उसमे 92 और क्रेयॉन डाल दी। अभी कितने क्रेयॉन हैं?",
    "एक होटल में 9 बर्गर थे और 4 हॉट डॉग्स । लेकिन उन्होंने 3 बर्गर बेचीं । अभी उनके पास कितने बर्गर बाकी हैं?",
    "इस साल 8 फूटबाल के मैच थे । 3 रात को खेले गए । कैथ 4 गेम जा नहीं पाया । कैथ कितने गेम गया?",
    "जोआन ने 15 डॉलर शॉर्ट्स पे खर्च किये और 14.82 डॉलर जैकेट पर । उसने 12.51 डॉलर शर्ट पर भी खर्च किये । वह कुल तीन शॉप में गयी । उसने कपड़ों पर कितने पैसे खर्च किये?",
    "पाई के लिए 6 डॉलर देने के बाद मैरी के पास अब 52 डॉलर हैं । उसके दोस्त के पास 43 डॉलर्स हैं. मैरी के पास पाई खरीद ने के पहले कितने पैसे थे?",
    "बखहार में 46 गांठे सूखी घास हैं । टॉम ने आज ही सूखी घास भरी थी । अभी बखहार में 60 गांठे हैं । उसने कितने गांठे भरी थी?",
    "मैरी केक बना रही हैं । रेसिपी के अनुसार 7 कप आटा और 3 कप चीनी की आवश्यकता हैं । उसने पहले से 2 कप आटा डाला हुआ था । उसे और कितने कप आटा डालना हैं?",
    "रेस्टोरेंट ने पाई के 7 भाग लंच के लिए और 5 भाग डिनर के लिए आज परोसा था । कल उन्होंने 8 भाग परोसा था । आज उन्होंने कितने भाग परोसे?",
    "डैन के बिल्ली के बच्चे हुआ और उनमेसे 5 के पास दाग थे । उन्होंने 7 अपने बच्चे टीम को दिया और 4 जैसन को । उसके पास अभी 5 बच्चे हैं । उसके पास कितने बिल्ली थे?",
    "सैली के पास बैंक mein 8 पैनी थे और 7 निकल । उसे पिताजी ने उसे 9 निकल दिए और उसके माताजी ने 2 निकल दिए । सैली के पास कितने निकल हैं?",
    "मैरी के पास 33 पोकेमोन कार्ड्स थे लेकिन उनमें से 5 फटे हुए थे । सैम ने उसे 23 नए कार्ड्स दिए । अब मैरी के पास कितने पोकेमोन कार्ड्स हैं?",
    "जोआन ने 24 कद्दू उगाये, कैथ ने 42 और अललयसा ने 13 । सबने मिलकर 34 दिन तक काम किया । उन्होंने मिलकर कितने कद्दू उगाये?",
    "फ्रेड के पास 10 लाल गुब्बारे हिअ, सैम के पास 46 लाल गुब्बारे और दान के पास 16 लाल गुब्बारे । गुब्बारे की कीमत 10 डॉलर हैं । उनके पास कितने लाल गुब्बारे हैं?",
    "बाग़ में 3 छोटे पेड़ हैं और 8 लम्बे । आज 9 और लम्बे पेड़ डाले जायेंगे । कल बाग़ में कितने छोटे पेड़ होंगे?",
    "कैथ ने 3 नाशपाती ली और जैसन ने 2 । जोआन ने 5 सेब भी लिए । कुल कितने नाशपाती ली गयी?",
    "ड्रावर में 5 कैंचियां और 3 पेंसिल हैं । जैसन ने और 4 कैंचियां डाली । अब कितने कैंचियां हैं?",
    "पिछले हफ्ते टीम के पास 12 डॉलर थी और कैथ के पास 36 डॉलर थी । टीम ने गाड़ियां धोयी और अब उस के पास 75 डॉलर्स हैं । टीम ने गाडी धोने के कितने पैसे लिए?",
    "टॉम ने एक बैटमैन गेम 13.60 डॉलर के लिए खरीदी और एक सुपरमैन गेम 5.06 डॉलर के लिए । टॉम के पास पहले से 2 गेम थी । टॉम ने उन गेम्स पर कितने पैसे लगाए?",
    "कैथ ने 6.51 डॉलर एक खरगोश के खिलोने पर खर्च किये, 5.79 डॉलर पेट के खाने के लिए और एक केज पर 12.51 डॉलर । उसे ज़मीन पर एक डॉलर पड़ा मिला । कैथ ने कुल कितने पैसे खर्च किये?",
    "मैरी ने लंच के लिये फ़ास्ट फ़ूड खाया । उसने 1,08 डॉलर सूप पे लगाए और 4.80 डॉलर सलाद पर । उसने 20 डॉलर के नोट के साथ पैसे दिए । मैरी ने खाने पे कितने पैसे खर्च किये?",
    "सैंडी के पास बैंक में 36 पैनी हैं और 31 निकल । उसके पिताजी ने उससे 20 निकल उधारी किये । अभी उसके पास कितने निकल हैं?",
    "जेसिका ने 35 तरबूज उगाये और 30 गाजर पर खरगोश 27 तरबूज खा गया । जेसिका के पास कितने तरबूज बाकी हैं?",
    "मिलने के पास 41 किताबे हैं और 31 मैगज़ीन । उसने काफी सारे किताबे खरीदी । अब उसके पास 87 किताबे हैं । उसने कितने किताबे खरीदी ?",
    "माइक इस साल 15 बास्केटबॉल गेम्स गया और 41 नहीं गया । वह पिछले साल 39 गेम्स गया था । माइक कितने गेम्स गया हुआ हैं ?",
    "नैंसी ने 2 प्याज उगाये, दान ने 9 और माइक ने 4 । उन्होंने 6 दिन तक काम किया । उन्होंने कितने प्याज उगाये?",
    "सारा के पास 3 हरे और 5 लाल गोलियां हैं । टॉम के पास 4 हरे गोलियां हैं । उनके पास कितने हरे गोलियां हैं?",
    "जेसिका केक बना रही हैं । रेसिपी के अनुसार 8 कप मैदा और 2 कप चीनी की जरुरत हैं । उसने पहले से 4 कप मैदा दाल दिया था । उसे और कितने कप डालने पड़ेंगे?",
    "सैली ने 12.32 डॉलर पीच पे खर्च किये 3 डॉलर के कूपन के बाद । उसने चेरी पर 1.54 डॉलर भी खर्च किये । उसने कितने पैसे खर्च किये?",
]

answers = [
                3120,
                1460,
                8317,
                523,
                5855,
                6029,
                5935,
                0.5,
                0.5,
                0.667,
                0.25,
                0.125,
                0.25,
                0.6,
                0.2,
                0.9,
                0.333,
                0.9,
                0.3,
                0.7,
                0.625,
                0.75,
                0.833,
                0.8,
                3.667,
                9.8,
                3.25,
                9.8,
                5.333,
                3.5,
                0.6,
                0.1,
                6699,
                5110,
                2713,
                43,
                6,
                26,
                13,
                10,
                18,
                18,
                51,
                58,
                55,
                83,
                21,
                34,
                3,
                15,
                6,
                74,
                9.43,
                34.72,
                14696,
                9844,
                64013,
                65134,
                106491,
                27004,
                5,
                3,
                3,
                5,
                6,
                88,
                12,
                8564,
                574,
                111421,
                9,
                138,
                118,
                6,
                4,
                42.33,
                58,
                36,
                2,
                9,
                16,
                13,
                56,
                79,
                28,
                3,
                5,
                9,
                63,
                18.66,
                25.81,
                7.64,
                11,
                11,
                46,
                54,
                10,
                12,
                4,
                16.89,
]

for i in range(0, len(sentences)):
    source.insert(i,(sentences[i], answers[i]))