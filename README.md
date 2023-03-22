# citytemp

Welcome! Thank you for visiting the weather-dash project repository.

If you're an avid traveller and you want to be prepared for the weather conditions at your next US destination, this app is for you!

[Link to the weather-dash app]()

To learn more about the app, you can jump to one of the sections below or keep scrolling.

* [Purpose and Motivation](#purpose-and-motivation)
* [Preview and Description](#dashboard-preview-and-description)
* [Installation](#installation)
* [Meet the Team](#meet-the-team)
* [Contributing](#contributing)
* [Support](#support)
* [Code of Conduct](#code-of-conduct)
* [License](#license)

## Purpose and Motivation

Being unprepared for certain weather conditions can make or break a trip. Our motivation with `weather-dash` was to create a reliable tool that US travelers can use to make informed decisions on which areas to visit and plan activities accordingly during their travels. Our app uses real historical data to assist travel enthusiasts in understanding weather fluctuations and temperatures across various states/cities in the United States and enables them to plan well for their upcoming trips to avoid weather disruptions and unwanted surprises.

## Proposal

Click [here](https://github.com/UBC-MDS/citytemp/blob/main/docs/proposal.md) to read the initial motivation and purpose of this dashboard.

## Dashboard Preview and Usage

<img src='img/demo.gif' width="1000" height="500">

Our dashboard presents observed temperature data from the [weather_forcasts.csv](https://github.com/rfordatascience/tidytuesday/blob/master/data/2022/2022-12-20/weather_forecasts.csv) in tidytuesday. It provides users with a single landing page which showcases visualizations of temperature data for various cities and states in the US.

First step for the users would be to select the state of their interest (eg. TX)

Based on the user selections, our app presents the following:

  - A bar plot showing the average temperatures(°C) in the selected state for each month. 
  - A violin plot depicting the distribution of temperatures in the cities of the selected state.

The user can also select two cities from the selected state from the drop downs available. Based on this, the app also presents a line plot comparing the temperature trend over the months in selected cities. Using these plots, the travellers can understand the overall average temperature in the selected state, how the temperature is varying in the cities of the selected state and also compare the temperature trends for two cities to choose the month and destination in US for their next trip and plan accordingly.

# Contributing

Feedback and suggestions are always welcome! 

Please read [the contributing guidelines](https://github.com/UBC-MDS/citytemp/blob/main/CONTRIBUTING.md)
to get started.

## Support

If you run into trouble, please [check the issue
list](https://github.com/UBC-MDS/citytemp/issues) to see
if your problem has already been reported or to open new issues.

## Code of conduct

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation. Detailed descriptions
of these points can be found in [`CODE_OF_CONDUCT.md`](https://github.com/UBC-MDS/citytemp/blob/main/CODE_OF_CONDUCT.md).

## License
The citytemp Dashboard is licensed under the terms of the MIT license.
