package io.github.ruzafa8.ft.avaj_launcher.flyable;

import io.github.ruzafa8.ft.avaj_launcher.WeatherTower;

public abstract class Flyable {
    protected WeatherTower weatherTower;

    public abstract void updateConditions();

    public void registerTower(WeatherTower weatherTower) {
        this.weatherTower = weatherTower;
        weatherTower.register(this);
    }

    public abstract String getCode();

    public WeatherTower getWeatherTower() {
        return weatherTower;
    }
}
