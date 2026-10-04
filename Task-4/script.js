/**
 * Digital Clock Script — VEDA Technology Web Development Internship Task 4
 * Objective: Practice JavaScript Date objects, timers, DOM selection and DOM updates.
 */

// Function to update the clock display with the current time
function updateClock() {
  // 1. Get current date and time using JavaScript Date object
  const now = new Date();

  // 2. Extract current hours, minutes, and seconds
  const hours = now.getHours();
  const minutes = now.getMinutes();
  const seconds = now.getSeconds();

  // 3. Add leading zeros if number is less than 10 (e.g., 9 -> "09")
  const formattedHours = hours < 10 ? '0' + hours : String(hours);
  const formattedMinutes = minutes < 10 ? '0' + minutes : String(minutes);
  const formattedSeconds = seconds < 10 ? '0' + seconds : String(seconds);

  // 4. Select DOM elements and update their text content
  const hoursElement = document.getElementById('hours');
  const minutesElement = document.getElementById('minutes');
  const secondsElement = document.getElementById('seconds');

  if (hoursElement) hoursElement.textContent = formattedHours;
  if (minutesElement) minutesElement.textContent = formattedMinutes;
  if (secondsElement) secondsElement.textContent = formattedSeconds;
}

// 5. Start clock immediately on page load to eliminate initial 1-second delay
updateClock();

// 6. Update the clock automatically every second (1000ms) using setInterval
setInterval(updateClock, 1000);
