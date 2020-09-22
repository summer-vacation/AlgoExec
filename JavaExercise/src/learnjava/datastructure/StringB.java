package learnjava.datastructure;


/***
 *  String
 *  StringBuilder
 *  StringBuffer    线程安全
 *
 *  StringBuilder 相较于 StringBuffer 有速度优势，所以多数情况下建议使用 StringBuilder 类。
 *  然而在应用程序要求线程安全的情况下，则必须使用 StringBuffer 类。
 */
public class StringB {

    public static void main(String args[]){
        StringBuffer sBuffer = new StringBuffer("菜鸟教程官网：");
        sBuffer.append("www");
        sBuffer.append(".runoob");
        sBuffer.append(".com");
        System.out.println(sBuffer);



    }
}
