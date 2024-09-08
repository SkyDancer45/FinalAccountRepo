const puppeteer = require('puppeteer');

async function automateWhatsApp() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.goto('https://web.whatsapp.com/');

  // Wait for the QR code to appear
  await page.waitForSelector('canvas');

  // Capture a screenshot of the QR code
  await page.screenshot({ path: 'qr_code.png' });

  // Close the browser
  await browser.close();
}

automateWhatsApp();
