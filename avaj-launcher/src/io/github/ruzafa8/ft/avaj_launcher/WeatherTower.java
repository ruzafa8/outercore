package io.github.ruzafa8.ft.avaj_launcher;

public class WeatherTower extends Tower {
    public String getWeather(Coordinates coordinates) {
        return WeatherProvider.getInstance().getCurrentWeather(coordinates);
    }

    @Override
    public void register(Flyable observer) {
        super.register(observer);
        observer.registerTower(this);
        System.out.println("Tower says: " + observer.getCode() + " registered to weather tower.");
    }

    @Override
    public void unregister(Flyable observer) {
        super.unregister(observer);
        observer.registerTower(null);
        System.out.println("Tower says: " + observer.getCode() + " unregistered to weather tower.");
    }

    public void changeWeather() {
        this.conditionChanged();
    }
}
