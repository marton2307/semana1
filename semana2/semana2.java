public class Semana_2 {
    
    int[] arreglos1 = new int[10];
    int[] arreglos2 =  {1,2,3,4};

    private Object[] arreglo3={"22",22,Boolean.FALSE,Long.parseLong("22")};
    private int[][][]=[1,1],[1,1,],[1,1];

    private Persona[]



    public static void main(String[] args) {
        Semana_2 clase = new Semana_2();
        clase.recorrido();
    }
    
    public void recorrido() {
        for(int dato : arreglos2) {
            System.out.println(dato);
        }
    }
}