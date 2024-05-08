def preprompt(user_input):
    preprompt = f"""Tu reçois le texte suivant : \n\n{user_input}\n\n 
    "Ce texte contient une date, une date des faits, le nom du collaborateur, et des faits.
     Tu dois prendre ce texte en entrée et générer un résumé qui reprend les éléments cités, et qui expose les faits de manière claire et concise. 
     Assure-toi d'inclure des formules de politesse au début et à la fin du texte.
     Transforme ce texte en entrée en demande de justification de la part du collaborateur 
     Voici un exemple de texte en sortie : 

     Exemple 1 : 

     Bonjour [nom du collaborateur], 
     Je souhaiterais que tu reviennes sur les circonstances concernant [].  
     Pouvez-vous m'expliquer ce qu'il s'est passé ?   
     Je te remercie d’avance pour toutes ces précisions.  
     [nom du signataire]

    Exemple 2:

    Bonjour Seddik, 
    Ce [date de l'incident] vous ne respectiez pas l’obligation de [obligation non respectée]
    Pouvez-vous m’expliquer ce qui a conduit au non-respect de cette règle ?  
    Dans l’attente de vous lire, 
    [nom du signataire]   

    
    """




    return preprompt