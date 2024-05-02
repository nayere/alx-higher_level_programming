$(document).ready(function() {
   
    function fetchAndDisplayGreeting() {
        // Get the language code from the input field
        const languageCode = $('#language_code').val();

        // Define the API URL, using the language code as a query parameter
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;


        $.get(apiUrl, function(response) {

            if (response && response.hello) {
          
                $('#hello').text(response.hello);
            } else {
                // If the response is invalid or does not contain the 'hello' key,
                // display an error message
                $('#hello').text('Error: Could not fetch greeting');
            }
        }).fail(function() {
            // Handle errors 
            $('#hello').text('Error: Could not fetch greeting');
        });
    }
