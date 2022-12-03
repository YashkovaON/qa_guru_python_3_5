from selene.support.shared import browser
from selene import be, have
from selene import command


def test_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Olga')
    browser.element('#lastName').type('YA')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('1234567891')
    browser.element('#userEmail').type('name@example.com')
    browser.element('[id="hobbies-checkbox-2"]').perform(command.js.scroll_into_view)
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#currentAddress').type('Moscow sity')
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="4"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1999"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--011"]').click()
    browser.element('#subjectsInput').type('Com').press_enter()
    browser.element('#uploadPicture').send_keys(rf'C:\Users\olgaya\Desktop\foto.jpg')
    browser.element('#submit').press_enter()

    browser.all('.table-responsive:nth-of-type(1) td').should(have.texts(
        'Student Name', 'Olga YA',
        'Student Email', 'name@example.com',
        'Gender', 'Female',
        'Mobile', '1234567891',
        'Date of Birth', '11 May,1999',
        'Subjects', 'Computer Science',
        'Hobbies', 'Reading',
        'Picture', 'foto.jpg',
        'Address', 'Moscow sity',
        'State and City', 'NCR Delhi'))
