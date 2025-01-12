package io.github.ruzafa8.ft.avaj_launcher;

public class Helicopter extends Aircraft {
    public Helicopter(long id, String name, Coordinates coordinates) {
        super(id, name, coordinates);
    }

    @Override
    public void updateConditions() {
        String weather = this.weatherTower.getWeather(this.coordinates);
        switch (weather) {
            case "SUN":
                this.coordinates.offsetCoordinates(10, 0, 2);
                System.out.println(getCode() + ": Helicopter, helicopter...");
                break;
            case "RAIN":
                this.coordinates.offsetCoordinates(5, 0, 0);
                System.out.println(getCode() + ": What a storm!!");
                break;
            case "FOG":
                this.coordinates.offsetCoordinates(1, 0, 0);
                System.out.println(getCode() + ": Mayday, mayday, mayday! A dense fog is surrounding us!");
                break;
            case "SNOW":
                this.coordinates.offsetCoordinates(0, 0, -12);
                System.out.println(getCode() + ": My rotor is going to freeze.");
                break;
        }
    }
}
