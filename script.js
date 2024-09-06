document.addEventListener('DOMContentLoaded', () => {
    const localTimezoneSelect = document.getElementById('local-timezone');
    const timezoneList = document.getElementById('timezone-list');
    const addTimezoneButton = document.getElementById('add-timezone');

    // Populate local time zone dropdown
    const timezones = ["UTC", "GMT", "EST", "CST", "MST", "PST"]; // Add more time zones as needed
    timezones.forEach(tz => {
        const option = document.createElement('option');
        option.value = tz;
        option.textContent = tz;
        localTimezoneSelect.appendChild(option);
    });

    addTimezoneButton.addEventListener('click', () => {
        const selectedTimezone = localTimezoneSelect.value;
        const timezoneItem = document.createElement('div');
        timezoneItem.textContent = selectedTimezone;
        timezoneList.appendChild(timezoneItem);
        // Here you would add logic to update the timeline
    });
});