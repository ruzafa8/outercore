package io.github.ruzafa8.ft.avaj_launcher;

public class JetPlane extends Aircraft {
    public JetPlane(long id, String name, Coordinates coordinates) {
        super(id, name, coordinates);
    }

    @Override
    public void updateConditions() {
        String weather = this.weatherTower.getWeather(this.coordinates);
        switch (weather) {
            case "SUN":
                this.coordinates.offsetCoordinates(0, 10, 2);
                System.out.println(getCode() + ": What a sunny day. :D");
                break;
            case "RAIN":
                this.coordinates.offsetCoordinates(0, 5, 0);
                System.out.println(getCode() + ": It's raining. Better watch out for lightings.");
                break;
            case "FOG":
                this.coordinates.offsetCoordinates(0, 1, 0);
                System.out.println(getCode() + ": This fog doesn't let me move on...");
                break;
            case "SNOW":
                this.coordinates.offsetCoordinates(0, 0, -7);
                System.out.println(getCode() + ": OMG! Winter is coming.");
                break;
        }
    }
}
