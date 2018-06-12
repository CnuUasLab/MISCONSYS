/*

 ***************************************************
 *     Main Electron logic for the Ground station  *
 *                                                 *
 *               Author: davidkroell               *
 *              Version: 1.0.0                     *
 *                                                 *
 ***************************************************

 */

const electron = require('electron');
//const remote = require('remote');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;

// Keep reference of main window because of GC
var mainWindow = null;

// Quit when all windows are closed
app.on('window-all-closed', function() {
    app.quit();
});

// When application is ready, create application window
app.on('ready', function() {

    // Create main window
    mainWindow = new BrowserWindow({
	name:    "MISCONSYS",
	width:   1500,
	height:  900,
	toolbar: false
    });

    // Target HTML file that will be opened in Window
    mainWindow.loadURL('file://' + __dirname + "/index.html");

    // Remove the default menu.
    mainWindow.setMenu(null);
    mainWindow.setResizable(false);

    // Uncomment to use Chrome developer tools
    mainWindow.webContents.openDevTools({mode : 'detach'});

    // Cleanup when window is closed
    mainWindow.on('closed', function() {
	mainWindow = null
    });

    // exit button functionality for the window.
    /* mainWindow.webContents.executeJavaScript(`

        document.getElementById("exit-btn").addEventListener("click", function (e) {
            var window = remote.getCurrentWindow();
            window.close();
        });

    `); */


});
