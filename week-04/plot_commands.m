plot(y'(:,1), y'(:,2), 'r+', 'LineWidth',2, 'MarkerEdgeColor', 'k', y2'(:,1), y2'(:,2), 'r+', 'LineWidth', 2, 'MarkerEdgeColor', 'b');title('Dipendenza di I_L da R_L - generatore di corrente', 'FontSize',16);xlabel('Resistenza di carico R_L [Ohm]','FontSize',16);ylabel('Corrente I_L (A)','FontSize', 16);grid ON

plot(y'(:,1), y'(:,2), 'r+', 'LineWidth',2, 'MarkerEdgeColor', 'k');title('Dipendenza di I_L da R_L - generatore di corrente', 'FontSize',16);xlabel('Resistenza di carico R_L [Ohm]','FontSize',16);ylabel('Corrente I_L (A)','FontSize', 16);grid ON

filename3 = "corrente_carico_su_res_carico_R3_2k.txt"; fid = fopen(filename3,"r");[y3, ny3] = fscanf(fid, '%f %8f', [2, Inf]);

plot(y'(:,1), y'(:,2), 'r+', 'LineWidth',2, 'MarkerEdgeColor', 'k', y2'(:,1), y2'(:,2), 'r+', 'LineWidth', 2, 'MarkerEdgeColor', 'b', y3'(:,1), y3'(:,2), 'r+', 'LineWidth', 2, 'MarkerEdgeColor', 'r');title('Dipendenza di I_L da R_L - generatore di corrente', 'FontSize',16);xlabel('Resistenza di carico R_L [Ohm]','FontSize',16);ylabel('Corrente I_L (A)','FontSize', 16);grid ON

filename4 = "corrente_carico_su_res_carico_R3_250.txt"; fid = fopen(filename4,"r");[y4, ny4] = fscanf(fid, '%f %8f', [2, Inf]);

plot(y'(:,1), y'(:,2), 'r+', 'LineWidth',2, 'MarkerEdgeColor', 'k', y2'(:,1), y2'(:,2), 'r+', 'LineWidth', 2, 'MarkerEdgeColor', 'b', y3'(:,1), y3'(:,2), 'r+', 'LineWidth', 2, 'MarkerEdgeColor', 'r', y4'(:,1), y4'(:,2), 'r+', 'LineWidth', 2, 'MarkerEdgeColor', 'g');title('Dipendenza di I_L da R_L - generatore di corrente', 'FontSize',16);xlabel('Resistenza di carico R_L [Ohm]','FontSize',16);ylabel('Corrente I_L (A)','FontSize', 16);grid ON

filename5= "corrente_carico_su_res_carico_R3_125_R1_4k.txt"; fid = fopen(filename5,"r");[y5, ny5] = fscanf(fid, '%f %8f', [2, Inf]);filename6= "corrente_carico_su_res_carico_R3_250_R1_2k.txt"; fid = fopen(filename6,"r");[y6, ny6] = fscanf(fid, '%f %8f', [2, Inf]);

plot(y5'(:,1), y5'(:,2), 'r+', 'LineWidth',2, 'MarkerEdgeColor', 'k',y6'(:,1), y6'(:,2), 'r+', 'LineWidth',2, 'MarkerEdgeColor', 'r', y'(:,1), y'(:,2), 'r+', 'LineWidth',2, 'MarkerEdgeColor', 'b');title('Dipendenza di I_L da R_L - generatore di corrente - dipendenza da R3 e R1', 'FontSize',16);xlabel('Resistenza di carico R_L [Ohm]','FontSize',16);ylabel('Corrente I_L (A)','FontSize', 16);grid ON

filename7 = "Vout_R_L_R3_500.txt"; fid = fopen(filename7,"r");[y7, ny7] = fscanf(fid, '%f %8f', [2, Inf]);
plot(y7'(:,1), y7'(:,2), 'r+', 'LineWidth',2, 'MarkerEdgeColor', 'k');title('Dipendenza di V_{out} da R_L - generatore di corrente', 'FontSize',16);xlabel('Resistenza di carico R_L [Ohm]','FontSize',16);ylabel('V_{out} (V)','FontSize', 16);grid ON