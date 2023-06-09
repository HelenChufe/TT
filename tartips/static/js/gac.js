var input = document.getElementById("myInput");
var list = document.getElementById("myUL");





input.addEventListener("input", function() {
  // Clear the suggestions list
  list.innerHTML = "";
  // Get the user input
  var inputVal = this.value;
  // Filter the suggestions based on the user input
  var filteredSuggestions = suggestions.filter(function(suggestion) {
    return suggestion.toLowerCase().indexOf(inputVal.toLowerCase()) !== -1;
  });
  // Add the filtered suggestions to the list
  filteredSuggestions.forEach(function(suggestion) {
    var li = document.createElement("li");
    li.textContent = suggestion;
    list.appendChild(li);
  });
});
 // Add event listeners to the list items
list.addEventListener("click", function(e) {
  if (e.target && e.target.nodeName === "LI") {
    // Set the input field value to the selected suggestion
    input.value = e.target.textContent;
    // Clear the suggestions list
    list.innerHTML = "";
  }
});
 // Add event listeners to the input field
input.addEventListener("focus", function() {
  list.classList.add("active");
});
 input.addEventListener("blur", function() {
  list.classList.remove("active");
});