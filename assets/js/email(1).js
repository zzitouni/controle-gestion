        (function(){
            emailjs.init("eMTxLrvfqMfqpOgrA"); 
        })();
        
        function envoyerEmailConfirmation(nomDestinataire, adresseDestinataire) {
            const templateParams = {
                destinataire: adresseDestinataire,
                sujet: "Confirmation de réception de votre réclamation",
                contenu: "Cher/Chère destinataire,\n\nNous vous remercions d'avoir pris le temps de soumettre votre réclamation...\n\nCordialement,\n+"+nomDestinataire+"\nLEONI"
            };

            emailjs.send('service_jkwhr7d', 'template_cy48mhd', templateParams)
                .then(function(response) {
                    alert('E-mail de confirmation envoyé avec succès !');
                }, function(error) {
                    console.error('Erreur lors de l\'envoi de l\'e-mail de confirmation :', error);
                    alert('Une erreur s\'est produite lors de l\'envoi de l\'e-mail de confirmation.');
                });
        }
