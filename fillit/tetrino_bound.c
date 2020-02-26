/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tetrino_bound.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: eric <eric@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/11/28 14:37:51 by etexier           #+#    #+#             */
/*   Updated: 2020/02/04 21:16:48 by eric             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "fillit.h"

static int			max_x(t_ushort t)
{
	int max;

	max = 4;
	if (!is_on(t, 3) && !is_on(t, 7) && !is_on(t, 11) && !is_on(t, 15))
	{
		max--;
		if (!is_on(t, 2) && !is_on(t, 6) && !is_on(t, 10) && !is_on(t, 14))
		{
			max--;
			if (!is_on(t, 1) && !is_on(t, 5) && !is_on(t, 9) && !is_on(t, 13))
				max--;
		}
	}
	return (max);
}

static int			min_y(t_ushort t)
{
	int miy;

	miy = 1;
	if ((t & 0xF000) == 0)
	{
		miy++;
		if ((t & 0xFF00) == 0)
		{
			miy++;
			if ((t & 0xFFF0) == 0)
				miy++;
		}
	}
	return (miy);
}

static void			bound_x(t_ushort t, int *x)
{
	int mix;

	mix = 1;
	if (!is_on(t, 0) && !is_on(t, 4) && !is_on(t, 8) && !is_on(t, 12))
	{
		mix++;
		if (!is_on(t, 1) && !is_on(t, 5) && !is_on(t, 9) && !is_on(t, 13))
		{
			mix++;
			if (!is_on(t, 2) && !is_on(t, 6) && !is_on(t, 10) && !is_on(t, 14))
				mix++;
		}
	}
	*x = max_x(t) - mix + 1;
}

static void			bound_y(t_ushort t, int *y)
{
	int may;

	may = 4;
	if ((t & 0x000F) == 0)
	{
		may--;
		if ((t & 0x00FF) == 0)
		{
			may--;
			if ((t & 0x0FFF) == 0)
				may--;
		}
	}
	*y = may - min_y(t) + 1;
}

void				bound(t_ushort t, int *x, int *y)
{
	bound_x(t, x);
	bound_y(t, y);
}
