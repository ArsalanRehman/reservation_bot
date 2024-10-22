const { Builder, By, until, Key } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const options = new chrome.Options();
options.addArguments('--no-sandbox');
options.addArguments('--disable-dev-shm-usage');
// Uncomment if you want headless mode
// options.addArguments('--headless');

// Path to your chromedriver
const service = new chrome.ServiceBuilder('/home/arslan/python_course/tenis/chromedriver');

// Set the ChromeDriver service to use the correct path
// chrome.setDefaultService(service.build());

async function run() {
    let driver = await new Builder()
        .forBrowser('chrome')
        .setChromeOptions(options)
        .build();

    try {
        // Open the URL
        await driver.get('https://tenis.randevu.sanliurfa.bel.tr/index.php');

        // Give the page some time to load (increase wait if necessary)
        await driver.sleep(5000);

        // Find all the elements with the desired class
        let elements = await driver.findElements(By.css('a.btn.btn-outline.btn-outline-dashed.btn-outline-success.btn-active-light-success.mb-2'));

        // Iterate over elements and click the one that says "15:00"
        for (let element of elements) {
            let text = await element.getText();
            if (text === "15:00") {
                await element.click();
                console.log("Clicked the 15:00 court availability!");
                break;
            }
        }

        await driver.sleep(2000); // Give some time for the modal to appear

        // Click the confirmation button on the modal
        let confirmButton = await driver.findElement(By.css('button.swal2-confirm.swal2-styled.swal2-default-outline'));
        await confirmButton.click();
        console.log("Clicked the confirmation button on the modal!");

        await driver.sleep(5000); // Wait for the next page to load

        // Fill in the form
        await driver.findElement(By.id("tc")).sendKeys("11111111111");
        await driver.findElement(By.id("adi")).sendKeys("Arslan");
        await driver.findElement(By.id("soyadi")).sendKeys("test soyadi");
        await driver.findElement(By.id("cep_telefonu")).sendKeys("05431111111");
        await driver.findElement(By.id("dogum_tarihi")).sendKeys("19/11/1998");

        // Select gender
        let genderSelect = await driver.findElement(By.id("cinsiyet"));
        let genderOptions = await genderSelect.findElements(By.tagName('option'));
        for (let option of genderOptions) {
            let text = await option.getText();
            if (text === "Kadın") {
                await option.click();
                break;
            }
        }

        // Fill in guest details
        await driver.findElement(By.id("konuk_dogum_tarihi")).sendKeys("20/11/1998");
        await driver.findElement(By.id("konuk_tc")).sendKeys("11111111111");
        await driver.findElement(By.id("konuk_adi")).sendKeys("test");
        await driver.findElement(By.id("konuk_soyadi")).sendKeys("test surname");

        // Check the checkbox if not already checked
        let checkbox = await driver.findElement(By.className("form-check-input"));
        let isChecked = await checkbox.isSelected();
        if (!isChecked) {
            await checkbox.click();
        }

        console.log("Form filled and checkbox checked!");

        // Submit the form
        let submitButton = await driver.findElement(By.css('button.btn.btn-block.btn-primary'));
        await submitButton.click();
        console.log("Form submitted!");

        // Wait for the page to process submission (60 seconds)
        await driver.sleep(60000);

    } finally {
        await driver.quit(); // Always close the driver at the end
    }
}

run();
