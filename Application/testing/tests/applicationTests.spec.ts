import { test, expect } from '@playwright/test';

//Pages
const dashboard_page = "http://127.0.0.1:5000/"
const login_page = "http://127.0.0.1:5000/login"
const signup_page = "http://127.0.0.1:5000/signup"
const welcome_page = "http://127.0.0.1:5000/welcome"

//Buttons
const login_btn = "[data-testid='login-btn']"
const signup_btn = "[data-testid='signup-btn']"
const post_btn = "[data-testid='post-btn']"

//Text Fields
const username = "[data-testid='username']"
const password = "[data-testid='password']"
const post_msg_box = "[data-testid='post-msg-box']"

//Login Credentials 
const admin_user = "Ishan"
const admin_pass = "Ishan101"
const test_user = "TestUser6"
const test_pass = "TestPass6"



test('dashboard login button', async ({ page }) => {
  /**
  This test checks that when the login button is clicked on the 
  dashboard, it takes you to the login page.

  pass: If the user lands on the login page
   */
  await page.goto(dashboard_page);
  page.click(login_btn)
  await expect(page).toHaveURL(login_page);
});

//--------------------------------------

test('dashboard signup button', async ({ page }) => {
  /**
  This test checks that when the signup button is clicked on the 
  dashboard, it takes you to the signup page.

  pass: If the user lands on the signup page
   */
  await page.goto(dashboard_page);
  page.click(signup_btn)
  await expect(page).toHaveURL(signup_page);
});

//--------------------------------------

test('login with admin cred', async ({ page }) => {
  /**
  This test checks that the user can login with admin 
  credentials.

  pass: If the user is on the welcome page.
   */
  await page.goto(dashboard_page);
  page.click(login_btn)
  await expect(page).toHaveURL(login_page);
  page.fill(username, admin_user)
  await page.waitForTimeout(1000);
  page.fill(password, admin_pass)
  page.click(login_btn)
  await expect(page).toHaveURL(welcome_page);

});

test('create an account', async ({ page }) => {
  /**
  This test checks that the user can create an account
  and sign in with the same credentials.

  pass: If the user can create and sign in using same credentials.
   */
  await page.goto(dashboard_page);
  page.click(signup_btn)
  await expect(page).toHaveURL(signup_page);
  page.fill(username, test_user)
  await page.waitForTimeout(1000);
  page.fill(password, test_pass)
  page.click(signup_btn)
  await expect(page).toHaveURL(dashboard_page);
  page.click(login_btn)
  await expect(page).toHaveURL(login_page);
  page.fill(username, test_user)
  await page.waitForTimeout(1000);
  page.fill(password, test_pass)
  page.click(login_btn)
  await expect(page).toHaveURL(welcome_page);
});

test('post a message', async ({ page }) => {
  /**
  This test checks that the user can login and 
  post a message on the global discussion board.

  pass: If message is successfully posted.
   */
  await page.goto(dashboard_page);
  page.click(login_btn)
  await expect(page).toHaveURL(login_page);
  page.fill(username, admin_user)
  await page.waitForTimeout(1000);
  page.fill(password, admin_pass)
  page.click(login_btn)
  await expect(page).toHaveURL(welcome_page);
  page.fill(post_msg_box, "Testing on video - Ishd Sharma")
  page.click(post_btn)
  await page.waitForTimeout(1000);
});