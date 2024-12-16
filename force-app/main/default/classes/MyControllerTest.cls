@isTest(seeAllData=true)
public with sharing class MyControllerTest {
    
    @isTest
    public static void test(){
        new MyController();
    }
}