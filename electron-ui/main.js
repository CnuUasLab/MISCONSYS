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
	width:   1400,
	height:  750,
	toolbar: false
    });

    // Target HTML file that will be opened in Window
    mainWindow.loadURL('file://' + __dirname + "./index.html");

    // Uncomment to use Chrome developer tools
    // mainWindow.webContents.openDevTools({detach:true});

    // Cleanup when window is closed
    mainWindow.on('closed', function() {
	mainWindow = null
    });
});
