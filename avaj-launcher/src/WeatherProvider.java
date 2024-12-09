class WeatherProvider {
    private static WeatherProvider instance;
    private String weather;

    private WeatherProvider() {}

    public String getCurrentWeather(Coordinates pCoordinates);

    public static WeatherProvider getInstance() {
        if (this.instance == null) {
            this.instance = new WeatherProvider();
        }
        return this.instance;
    }
}
