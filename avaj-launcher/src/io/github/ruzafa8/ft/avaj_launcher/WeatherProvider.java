package io.github.ruzafa8.ft.avaj_launcher;

public class WeatherProvider {
    private static WeatherProvider instance;
    private String weather;

    private WeatherProvider() {}

    public String getCurrentWeather(Coordinates coordinates) {
        return "TO DO";
    }

    public static WeatherProvider getInstance() {
        if(instance == null) {
            instance = new WeatherProvider();
        }
        return instance;
    }
}
