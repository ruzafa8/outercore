package io.github.ruzafa8.ft.avaj_launcher;

public class Coordinates {
    private int longitude;
    private int latitude;
    private int height;

    public Coordinates(int longitude, int latitude, int height) {
        this.longitude = longitude;
        this.latitude = latitude;
        this.height = height;
    }

    public int getLongitude() {
        return this.longitude;
    }

    public int getLatitude() {
        return this.latitude;
    }

    public int getHeight() {
        return this.height;
    }

    public void offsetCoordinates(int longitudeOffset, int latitudeOffset, int heightOffset) {
       this.longitude += longitudeOffset;
       this.latitude += latitudeOffset;
       this.height += heightOffset;
       if (this.height < 0) {
           this.height = 0;
       }
       if (this.height > 100) {
           this.height = 100;
       }
    }
}
