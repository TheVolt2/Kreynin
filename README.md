## Flet Counter Example

This example demonstrates how to create a simple counter using Flet.

### Overview

The main function is the entry point of the application. It creates a new page with a title and sets the vertical alignment to center.

A TextField widget is created to display the counter value. Three IconButton widgets are created for the minus, plus, and reset actions.

Event handlers are defined for each button to handle the minus, plus, and reset actions. The minus_click handler decrements the counter value, the plus_click handler increments the counter value, and the reset_click handler resets the counter value to 0.

A save_result function is defined to save the current counter value to a file.

The page.add method is used to add the widgets to the page. The widgets are arranged in a Column widget with two Row widgets inside. The Row widgets contain the buttons and the TextField.

### Running the Example

To run the example, you can use the following steps:

1. Install Flet using pip install flet.
2. Create a new Python file and paste the code into it.
3. Run the Python file using python filename.py.

### Output

When you run the example, you will see a page with a counter that you can increment, decrement, or reset. You can also save the current counter value to a file.

### Conclusion

This example demonstrates the basics of creating a simple counter using Flet. You can use this as a starting point to create more complex applications.
