class RideSharingSystem {
    LinkedList<Integer> drivers = new LinkedList<>();
    LinkedList<Integer> riders = new LinkedList<>();
    HashSet<Integer>ridc;
    public RideSharingSystem() {
        ridc = new HashSet<>();
        
    }
    
    public void addRider(int riderId) {
        riders.addLast(riderId);
        ridc.add(riderId);
    }
    
    public void addDriver(int driverId) {
        drivers.addLast(driverId);
    }
    
    public int[] matchDriverWithRider() {
        while(riders.size() != 0 && !ridc.contains(riders.peekFirst())){
            riders.pollFirst();
        }
        if(riders.size() == 0 || drivers.isEmpty()){
            return new int[]{-1,-1};
        }
        int rider = riders.pollFirst();
        int driver = drivers.pollFirst();


        return new int[]{driver,rider} ;
    }
    
    public void cancelRider(int riderId) {
        if(ridc.contains(riderId)){
            ridc.remove(riderId);
        }
    }
}

