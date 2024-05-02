$(document).ready(function() {
    // Event listener for the 'Translate' button click
    $('#btn_translate').click(function() {
        // Get the language code from the input field
        const languageCode = $('#language_code').val();

        // Define the API URL, using the language code as a query parameter
        const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

        // Make an AJAX request to the API
        $.get(apiUrl, function(response) {
            // Check if the response contains the 'hello' key
            if (response && response.hello) {
                // Update the DIV#hello with the translated greeting
                $('#hello').text(response.hello);
            } else {
                // If the response is invalid or does not contain the 'hello' key,
                // display an error message
                $('#hello').text('Error: Could not fetch greeting');
            }
        }).fail(function() {
            // Handle errors (e.g., network issues)
            $('#hello').text('Error: Could not fetch greeting');
        });
    });
});
