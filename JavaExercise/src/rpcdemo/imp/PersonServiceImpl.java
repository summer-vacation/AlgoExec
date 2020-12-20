package rpcdemo.imp;

import rpcdemo.anno.RpcService;


@RpcService(PersonService.class)
public class PersonServiceImpl implements PersonService{

	public Person getInfo() {
		Person person = new Person();
		person.setAge(22);
		person.setName("qjm");
		person.setSex("男");
		return person;
	}

	public boolean printInfo(Person person) {
		if(person != null){
			System.out.println(person);		// 服务端输出
			return true;
		}
		return false;
	}

}
