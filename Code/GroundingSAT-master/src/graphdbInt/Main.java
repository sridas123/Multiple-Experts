package graphdbInt;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String path = "./data/";
		String FactFile = path+args[0];
		String RWFile = path+args[1];
		String exFile = path+args[2];
		//String negFile = path+args[4];
		String outputFileName = path+args[3];
		String dbName = args[4];
		
		try
		{
			final long startTime = System.nanoTime();
			FileOutputStream OutPut = new FileOutputStream(outputFileName);
			GraphDB gdb = new GraphDB(FactFile,null,"ddi2",true);
			//System.exit(1);
			BufferedReader br = new BufferedReader(new FileReader(new File(RWFile)));
			String line = "";
			String encloser = "[\n"; String endAll = "\n]";
			OutPut.write(encloser.getBytes());
			int i=0;
			while((line = br.readLine())!=null)
			{
				//if(i>2)
					//break;
				line=line.substring(0, line.length()-6);
				System.out.println(line);
				String head = line.split(":-")[0].trim();
				String body = line.split(":-")[1].trim();
				String[] preds = body.split("\\;");
				String vars = head.trim().split("\\(")[1].replaceAll("\\)", "").trim();
				System.out.println("Grounded Variables:"+vars);
				

				BufferedReader brex = new BufferedReader(new FileReader(new File(exFile)));
				String ex;
				while((ex = brex.readLine())!=null)
				{
					ex = ex.substring(0, ex.length()-1);
					System.out.println(ex);
					String vals = ex.split("\\(")[1].replaceAll("\\)", "").trim();
					System.out.println("Groundings:"+vals);
					String start = "Ex: "+ex+"   RW: "+line;
					OutPut.write(start.getBytes());
					//OutPut.write(System.getProperty("line.separator").getBytes());
					
					/*
					 * For partial groundings 
					 * Provide comma delimited string of variable names in first argument
					 * and comma separated values of variables in the correct order
					 */
					String ret = gdb.getGroundings(vars, vals, preds, OutPut);  
					
					
					//OutPut.write(ret.getBytes());
					//System.out.println(ret);
					//String end = " \n ";
					OutPut.write(System.getProperty("line.separator").getBytes());
					i++;
					System.out.println(i);
				}

				brex.close();
			}
			OutPut.write(endAll.getBytes());
			//gdb.close();
			OutPut.close();
			//System.out.println("here");
			//BufferedReader new_br = new BufferedReader(new FileReader(new File(outputFileName)));
			br.close();
			final long duration = System.nanoTime() - startTime;
			System.out.println(duration);
			
		} 
		catch (Exception e) 
		{
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
	}

}
