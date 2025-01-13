package io.github.ruzafa8.ft.avaj_launcher;

public class WeatherProvider {
    private static WeatherProvider instance;
    private final String[] weather;

    private WeatherProvider() {
        weather = new String[] { "SUN", "RAIN", "FOG", "SNOW" };
    }

    public String getCurrentWeather(Coordinates coordinates) {
        return weather[
            (coordinates.getHeight() + coordinates.getLatitude() + coordinates.getLongitude()) % weather.length
        ];
    }

    public static WeatherProvider getInstance() {
        if (instance == null) {
            instance = new WeatherProvider();
        }
        return instance;
    }
}
