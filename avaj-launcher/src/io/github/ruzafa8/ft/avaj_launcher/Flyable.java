package io.github.ruzafa8.ft.avaj_launcher;

public abstract class Flyable {
    protected WeatherTower weatherTower;

    public abstract void updateConditions();

    public void registerTower(WeatherTower weatherTower) {
        this.weatherTower = weatherTower;
    }

    protected abstract String getCode();
}
