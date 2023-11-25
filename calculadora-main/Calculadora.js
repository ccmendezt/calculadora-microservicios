class Calculadora {
    
    fetchOperation(tipo, numero1, numero2) {
        // Replace the URL with the actual URL where your Flask app is running
        const apiUrl = `http://127.0.0.1:5000/${tipo}/${numero1}/${numero2}`;
        // Make a GET request to the Flask route
        return fetch(apiUrl)
            .then(response => {
                // Check if the request was successful (status code 200-299)
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
    
                // Parse the response as JSON (assuming it returns JSON)
                return response.text();
            })
            .then(data => {
                // Handle the data
                console.log('Result:', data);
                return data;
            })
            .catch(error => {
                // Handle errors
                console.error('Fetch error:', error);
                throw error;
            });
    }

    sumar(num1, num2) {
        console.log('suma: ',this.fetchOperation('suma',num1, num2))
        return this.fetchOperation('suma',num1, num2)
        
    }

    restar(num1, num2) {
        return this.fetchOperation('resta',num1, num2)
    }

    dividir(num1, num2) {
        return this.fetchOperation('division',num1, num2)
    }

    multiplicar(num1, num2) {
        return this.fetchOperation('multiplicacion',num1, num2)
    }

    potencia(num1, num2) {
        return this.fetchOperation('potencia',num1, num2)
    }
    
} 