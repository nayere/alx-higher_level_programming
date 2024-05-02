// Select the UL element with the class 'my_list'
$(document).ready(function() {
    
    const myList = $('ul.my_list');

    // When the 'add_item' div is clicked, add a new <li> element to the list
    $('#add_item').click(function() {
        // Create a new <li> element with the text "Item"
        const newItem = $('<li>Item</li>');
        // Append the new <li> element to the list
        myList.append(newItem);
    });

    // When the 'remove_item' div is clicked, remove the last <li> element from the list
    $('#remove_item').click(function() {
        // Select the last <li> element and remove it
        myList.children().last().remove();
    });

    // When the 'clear_list' div is clicked, remove all <li> elements from the list
    $('#clear_list').click(function() {
        // Clear all elements from the list
        myList.empty();
    });
});
