package graphdbInt;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;

public class GenerateSchema {

	public static void generateSchema(String loc, String bkFile)
	{
		try{
		File f = new File(loc+bkFile);
		File fNew = new File(loc+"/schema.db");
		BufferedReader bf = new BufferedReader(new FileReader(f));
		BufferedWriter bw = new BufferedWriter(new FileWriter(fNew));
		String line = null;
		while((line = bf.readLine())!=null)
		{
			if(line.toLowerCase().contains("mode"))
			{
				String toWrite = line.replaceAll("mode: ", "");
				String[] components = toWrite.split("\\(");
				components[1] = components[1].replaceAll("\\)", "");
				String[] args = components[1].split(",");
				String finalstring = components[0]+'(';
				for(int i = 0;i<args.length;i++)
				{
					finalstring = finalstring + args[i].replaceAll("+", "").replaceAll("-", "").replaceAll("#", "");
				}
				finalstring = finalstring+')'+"\n";
				bw.write(finalstring);
			}
		}
		bf.close();
		bw.close();
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
}
