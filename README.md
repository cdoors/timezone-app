# TimeZone Comparison Tool

This simple application allows users to compare different time zones on a horizontal timeline. Users can select their local time zone and multiple other time zones to see how they align.

## Features

- Select a local time zone
- Add multiple time zones for comparison
- View a horizontal timeline displaying the selected time zones
- Simple and intuitive user interface

## Technologies Used

- HTML5
- CSS3
- JavaScript
- Moment.js (for time zone calculations)

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/timezone-comparison-tool.git
   ```

2. Navigate to the project directory:
   ```
   cd timezone-comparison-tool
   ```

3. To run the application locally for development purposes:
   - If you have Python installed, you can use Python's built-in HTTP server:
     - For Python 3.x:
       ```
       python -m http.server
       ```
     - For Python 2.x:
       ```
       python -m SimpleHTTPServer
       ```
   - If you have Node.js installed, you can use a package like `http-server`:
     - Install `http-server` globally:
       ```
       npm install -g http-server
       ```
     - Run the server:
       ```
       http-server
       ```
   - Open your web browser and navigate to `http://localhost:8000` (or the port number provided by your chosen method).

4. Alternatively, you can simply open `index.html` directly in your web browser, but some features might not work correctly due to browser security restrictions when running from a local file.

## Usage

1. Select your local time zone from the dropdown menu.
2. Click the "Add Time Zone" button to add more time zones for comparison.
3. Use the dropdown menus to select the desired time zones.
4. The horizontal timeline will update automatically to show the current time in each selected time zone.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
