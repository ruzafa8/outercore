abstract class Flyable {
    protected WeatherTower weatherTower;

    public abstract void updateConditions();

    public void registerTower(WeatherTower pTower) {
        this.weatherTower = weatherTower;
    }
}
